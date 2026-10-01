#!/usr/bin/env python3
"""Check documentation structure and selected explicit Tranzit regressions.

Uses only the Python standard library. This is not a game/simulation test suite
and cannot prove semantic consistency of arbitrary natural-language design.
"""
from __future__ import annotations

import argparse
import calendar
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

NUMBERED = re.compile(r'^#{1,6}\s+(\d+(?:\.\d+)*)\.?\s+', re.MULTILINE)
HEADING = re.compile(r'^#{1,6}\s+(.+?)\s*#*$', re.MULTILINE)
SECTION_REF = re.compile(r'\bSections?\s+(\d+(?:\.\d+)*(?:(?:\s*[,–-]\s*|\s+and\s+)\d+(?:\.\d+)*)*)')
LINK = re.compile(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)')
TABLE_ID = re.compile(r'^\|\s*([A-Z]+-\d{2})(?=\s|\|)', re.MULTILINE)
GOLDEN_ID = re.compile(r'^###\s+(G-\d{2})\b', re.MULTILINE)


@dataclass(frozen=True)
class Result:
    files: int
    headings: int
    links: int
    scenario_ids: int
    errors: tuple[str, ...]


def without_fences(text: str) -> str:
    """Blank fenced-code lines while keeping diagnostic line numbers stable."""
    result: list[str] = []
    fence_char = ''
    fence_length = 0
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if not fence_char:
            if marker:
                fence_char, fence_length = marker[1][0], len(marker[1])
                result.append('\n')
            else:
                result.append(line)
        else:
            if marker and marker[1][0] == fence_char and len(marker[1]) >= fence_length:
                fence_char = ''
            result.append('\n')
    return ''.join(result)


def heading_anchors(text: str) -> set[str]:
    """GitHub-style anchors for the simple ATX headings used in this repo."""
    used: set[str] = set()
    for match in HEADING.finditer(without_fences(text)):
        title = re.sub(r'<[^>]+>', '', match[1]).lower()
        base = re.sub(r'[^\w\s-]', '', title, flags=re.UNICODE).replace(' ', '-')
        anchor = base
        suffix = 0
        while anchor in used:
            suffix += 1
            anchor = f'{base}-{suffix}'
        used.add(anchor)
    return used


def source_to_game(year: int, month: int, day: int) -> tuple[int, int, int]:
    """Reference authoring conversion only, never runtime calendar arithmetic."""
    source = date(year, month, day)  # Validates Gregorian source, including leap days.
    length = calendar.monthrange(source.year, source.month)[1]
    return source.year, source.month, 1 + (source.day - 1) * 14 // length


def document_errors(name: str, text: str, *, core: bool = False) -> list[str]:
    clean = without_fences(text)
    errors: list[str] = []
    numbers = NUMBERED.findall(clean)
    for number, count in Counter(numbers).items():
        if count > 1:
            errors.append(f'{name}: duplicate section {number}')
    ids = TABLE_ID.findall(clean) + GOLDEN_ID.findall(clean)
    for identifier, count in Counter(ids).items():
        if count > 1:
            errors.append(f'{name}: duplicate requirement/scenario {identifier}')
    if core:
        for match in SECTION_REF.finditer(clean):
            line = clean.count('\n', 0, match.start()) + 1
            for number in re.findall(r'\d+(?:\.\d+)*', match[1]):
                if number not in numbers:
                    errors.append(f'{name}:{line}: missing core section {number}')
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', clean)]
    eligible = [p for p in paragraphs if len(p) >= 300 and not p.startswith(('|', '#', '-', '*', '>'))]
    for paragraph, count in Counter(eligible).items():
        if count > 1:
            errors.append(f'{name}: repeated long prose paragraph: {paragraph[:75]!r}')
    return errors


def check_repository(root: Path, *, enforce_contract: bool = True) -> Result:
    root = root.resolve()
    paths = sorted(set(root.glob('*.md')) | set((root / 'docs').rglob('*.md')))
    texts: dict[Path, str] = {}
    errors: list[str] = []
    for path in paths:
        try:
            texts[path.resolve()] = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append(f'{path.relative_to(root)}: cannot read UTF-8: {exc}')
    total_links = total_headings = scenario_ids = 0
    for path, text in texts.items():
        name = str(path.relative_to(root))
        clean = without_fences(text)
        total_headings += len(NUMBERED.findall(clean))
        scenario_ids += len(TABLE_ID.findall(clean)) + len(GOLDEN_ID.findall(clean))
        errors.extend(document_errors(name, text, core=name == 'docs/GAME_DESIGN.md'))
        for match in LINK.finditer(clean):
            raw = match[1]
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc:
                continue
            total_links += 1
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(root):
                errors.append(f'{name}: local link escapes repository: {raw}')
            elif not target.exists():
                errors.append(f'{name}: missing local link target: {raw}')
            elif parsed.fragment and target.suffix == '.md':
                target_text = texts.get(target)
                if target_text is None:
                    try:
                        target_text = target.read_text(encoding='utf-8')
                    except (OSError, UnicodeError) as exc:
                        errors.append(f'{name}: unreadable link target {raw}: {exc}')
                        continue
                if unquote(parsed.fragment) not in heading_anchors(target_text):
                    errors.append(f'{name}: missing heading anchor: {raw}')
    if enforce_contract:
        def content(name: str) -> str:
            value = texts.get(root / name)
            if value is None:
                errors.append(f'Missing required document: {name}')
            return value or ''
        core = content('docs/GAME_DESIGN.md')
        scope = content('docs/V1_SCOPE.md')
        readme = content('README.md')
        pipeline = content('docs/DATA_PIPELINE.md')
        required_sections = {'3.4', '11.0.1', '11.9', '15.11', '18.2', '32.2'}
        if not required_sections <= set(NUMBERED.findall(core)):
            errors.append('Canonical mechanics sections are missing')
        for phrase in ('**14 days per month**', '**168 days per year**', '**one real second equals one game minute**', '**0.5×, 1×, 2×, 4×, 8× and 16×**'):
            if phrase not in core:
                errors.append(f'Shared clock contract missing: {phrase}')
        for phrase in ('CargoBatch', 'The exact real-date-to-game-date mapping is still to be specified', 'The volume of onboard ticket sales itself does not add station dwell time'):
            if phrase in core:
                errors.append(f'Known obsolete core wording returned: {phrase}')
        for phrase in (
            'CONNECTION_AGREEMENTS.md',
            'protected connections missed',
            'protected-connection success',
            'connection-hold limit',
            'protected itinerary under Section 32.4',
            'Passenger connection-agreement mechanics remain required V1 design work',
        ):
            if phrase in core:
                errors.append(f'Removed passenger-connection mechanic returned: {phrase}')
        if (root / 'docs/CONNECTION_AGREEMENTS.md').exists():
            errors.append('Removed passenger connection-agreement specification returned')
        if 'Only 1900 is implemented' in readme:
            errors.append('README falsely describes the design-only preset as implemented')
        for anchor in ('#119-shipments-and-physical-cargo-lots', '#1511-enduring-historical-vehicle-availability'):
            if anchor not in scope:
                errors.append(f'V1 scope must point to canonical mechanics: {anchor}')
        if 'gregorian-month-proportional-v1' not in pipeline:
            errors.append('Missing versioned source-date conversion')
        # Ensure an omission cannot silently remove a subsystem from the ledger.
        expected = {f'SYS-{i:02d}' for i in range(1, 17)}
        for name in ('docs/V1_IMPLEMENTATION_BRIEF.md', 'docs/IMPLEMENTATION_STATUS.md'):
            found = {x for x in TABLE_ID.findall(content(name)) if x.startswith('SYS-')}
            if found != expected:
                errors.append(f'{name}: SYS-01..SYS-16 coverage differs: {sorted(found ^ expected)}')
        acceptance = content('docs/V1_ACCEPTANCE_TESTS.md')
        ids = set(TABLE_ID.findall(acceptance))
        for identifier in ('C-19', 'C-20', 'C-21', 'C-22', 'N-15', 'N-16', 'N-17', 'N-18', 'V-15', 'V-16', 'V-17', 'F-17', 'F-18', 'F-19', 'F-20', 'F-21', 'W-15', 'W-16'):
            if identifier not in ids:
                errors.append(f'Missing audit regression scenario: {identifier}')
    return Result(len(texts), total_headings, total_links, scenario_ids, tuple(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = check_repository(args.root)
    for error in result.errors:
        print(f'ERROR: {error}', file=sys.stderr)
    state = 'FAIL' if result.errors else 'PASS'
    print(f'{state}: {result.files} Markdown files, {result.headings} numbered headings, '
          f'{result.links} local links, {result.scenario_ids} scenario/requirement definitions; '
          f'{len(result.errors)} errors. Documentation checks only; game tests NOT RUN.')
    return 1 if result.errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
