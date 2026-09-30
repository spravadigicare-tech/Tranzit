"""Self-tests for the documentation validator, not tests of the future game."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_docs import check_repository, document_errors, heading_anchors, source_to_game, without_fences


class StructureTests(unittest.TestCase):
    def test_duplicate_numbered_heading(self):
        self.assertTrue(document_errors('x', '## 1. One\n## 1. Other\n'))

    def test_valid_core_reference(self):
        self.assertEqual(document_errors('x', '## 1. One\n### 1.1 Two\nSee Sections 1 and 1.1.\n', core=True), [])

    def test_missing_core_reference(self):
        self.assertTrue(document_errors('x', '## 1. One\nSee Section 2.\n', core=True))

    def test_range_endpoint_reference(self):
        self.assertTrue(document_errors('x', '## 1. One\nSee Sections 1–3.\n', core=True))

    def test_duplicate_scenario_id(self):
        self.assertTrue(document_errors('x', '| F-01 | First |\n| F-01 | Second |\n'))

    def test_references_do_not_redefine_scenario(self):
        self.assertEqual(document_errors('x', '| F-01 | First |\nSee F-01 and F-01.\n'), [])

    def test_duplicate_golden_journey(self):
        self.assertTrue(document_errors('x', '### G-01 — First\n### G-01 — Second\n'))

    def test_fenced_examples_ignored(self):
        source = '## 1. Real\n```text\n## 1. Example\nSee Section 99.\n```\n'
        self.assertEqual(document_errors('x', source, core=True), [])
        self.assertEqual(source.count('\n'), without_fences(source).count('\n'))

    def test_tilde_fence_ignored(self):
        self.assertNotIn('99', without_fences('~~~\nSee Section 99\n~~~\n'))

    def test_anchors_and_duplicate_suffixes(self):
        self.assertEqual(heading_anchors('# Hello world\n## Hello world\n### 11.9 Cargo\n'), {'hello-world', 'hello-world-1', '119-cargo'})

    def test_repeated_long_prose(self):
        paragraph = 'A meaningful requirement. ' * 20
        self.assertTrue(document_errors('x', paragraph + '\n\n' + paragraph))

    def test_short_repeated_labels_allowed(self):
        self.assertEqual(document_errors('x', 'Example:\n\nExample:\n'), [])


class LinkTests(unittest.TestCase):
    def check(self, text, other=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text(text, encoding='utf-8')
            if other is not None:
                (root / 'other.md').write_text(other, encoding='utf-8')
            return check_repository(root, enforce_contract=False)

    def test_existing_file_and_anchor(self):
        self.assertFalse(self.check('[ok](other.md#target)', '## Target\n').errors)

    def test_missing_file(self):
        self.assertTrue(self.check('[bad](missing.md)').errors)

    def test_missing_anchor(self):
        self.assertTrue(self.check('[bad](other.md#absent)', '## Target\n').errors)

    def test_external_link_not_fetched(self):
        self.assertFalse(self.check('[external](https://example.invalid/test)').errors)

    def test_fenced_link_not_checked(self):
        self.assertFalse(self.check('```\n[example](missing.md)\n```\n').errors)

    def test_escape_rejected(self):
        self.assertTrue(self.check('[outside](../outside.md)').errors)

    def test_missing_required_contract_files(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertTrue(check_repository(Path(directory)).errors)


class DateReferenceTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(source_to_game(1900, 1, 1), (1900, 1, 1))
        self.assertEqual(source_to_game(1900, 1, 14), (1900, 1, 6))
        self.assertEqual(source_to_game(1900, 1, 31), (1900, 1, 14))
        self.assertEqual(source_to_game(1900, 2, 28), (1900, 2, 14))
        self.assertEqual(source_to_game(2000, 2, 29), (2000, 2, 14))

    def test_invalid_dates_rejected(self):
        for value in ((1900, 2, 29), (1900, 4, 31), (1900, 13, 1), (1900, 1, 0)):
            with self.subTest(value=value), self.assertRaises(ValueError):
                source_to_game(*value)

    def test_all_month_lengths_monotonic_and_cover_14_days(self):
        import calendar
        for year in (1900, 2000, 2025, 2026):
            for month in range(1, 13):
                length = calendar.monthrange(year, month)[1]
                values = [source_to_game(year, month, day)[2] for day in range(1, length + 1)]
                self.assertEqual(values, sorted(values))
                self.assertEqual(set(values), set(range(1, 15)))


if __name__ == '__main__':
    unittest.main()
