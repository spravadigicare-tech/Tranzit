#!/usr/bin/env python3
"""Validate Tranzit's versioned vehicle content authoring data.

Uses only the Python standard library. This checks structural/cross-reference
invariants; it does not prove historical accuracy, balancing quality, art
completeness, or gameplay implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import sys
from typing import Any


@dataclass(frozen=True)
class VehicleContentResult:
    files: int
    manufacturers: int
    support_families: int
    market_profiles: int
    equipment_groups: int
    equipment_options: int
    templates: int
    models: int
    errors: tuple[str, ...]


def _read_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: cannot read valid UTF-8 JSON: {exc}")
        return {}


def _duplicates(values: list[str]) -> set[str]:
    seen: set[str] = set()
    dup: set[str] = set()
    for value in values:
        if value in seen:
            dup.add(value)
        seen.add(value)
    return dup


def _walk_forbidden(value: Any, *, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key == "available_until":
                errors.append(f"{child_path}: forbidden hard availability gate")
            _walk_forbidden(child, path=child_path, errors=errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _walk_forbidden(child, path=f"{path}[{index}]", errors=errors)


def check_vehicle_content(root: Path) -> VehicleContentResult:
    root = root.resolve()
    base = root / "content" / "vehicles"
    errors: list[str] = []
    if not base.exists():
        return VehicleContentResult(0, 0, 0, 0, 0, 0, 0, 0, ("Missing content/vehicles directory",))

    required = {
        "manufacturers.v1.json",
        "support_families.v1.json",
        "regional_market_profiles.v1.json",
        "equipment_options_1900.v1.json",
        "built_in_templates_1900.v1.json",
        "vehicle_models_1900.v1.json",
        "opening_market_1900.v1.json",
        "vehicle_model.schema.v1.json",
    }
    for name in sorted(required):
        if not (base / name).exists():
            errors.append(f"content/vehicles/{name}: missing required vehicle-content file")

    json_paths = sorted(base.glob("*.json"))
    docs = {p.name: _read_json(p, errors) for p in json_paths}
    for name, data in docs.items():
        _walk_forbidden(data, path=f"content/vehicles/{name}", errors=errors)

    manufacturers_doc = docs.get("manufacturers.v1.json", {})
    manufacturers = manufacturers_doc.get("manufacturers", []) if isinstance(manufacturers_doc, dict) else []
    manufacturer_ids = [x.get("id") for x in manufacturers if isinstance(x, dict) and isinstance(x.get("id"), str)]
    for duplicate in sorted(_duplicates(manufacturer_ids)):
        errors.append(f"manufacturers.v1.json: duplicate manufacturer id {duplicate}")
    manufacturer_set = set(manufacturer_ids)
    plant_ids = {
        plant
        for manufacturer in manufacturers
        if isinstance(manufacturer, dict)
        for plant in manufacturer.get("plant_ids", [])
        if isinstance(plant, str)
    }

    support_doc = docs.get("support_families.v1.json", {})
    support = support_doc.get("support_families", []) if isinstance(support_doc, dict) else []
    support_ids = [x.get("id") for x in support if isinstance(x, dict) and isinstance(x.get("id"), str)]
    for duplicate in sorted(_duplicates(support_ids)):
        errors.append(f"support_families.v1.json: duplicate support id {duplicate}")
    support_set = set(support_ids)

    market_doc = docs.get("regional_market_profiles.v1.json", {})
    profiles = market_doc.get("profiles", []) if isinstance(market_doc, dict) else []
    profile_ids = [x.get("id") for x in profiles if isinstance(x, dict) and isinstance(x.get("id"), str)]
    for duplicate in sorted(_duplicates(profile_ids)):
        errors.append(f"regional_market_profiles.v1.json: duplicate profile id {duplicate}")
    profile_set = set(profile_ids)

    equipment_doc = docs.get("equipment_options_1900.v1.json", {})
    groups = equipment_doc.get("groups", []) if isinstance(equipment_doc, dict) else []
    group_ids = [x.get("id") for x in groups if isinstance(x, dict) and isinstance(x.get("id"), str)]
    for duplicate in sorted(_duplicates(group_ids)):
        errors.append(f"equipment_options_1900.v1.json: duplicate group id {duplicate}")
    group_set = set(group_ids)
    option_to_group: dict[str, str] = {}
    option_ids: list[str] = []
    for group in groups:
        if not isinstance(group, dict):
            continue
        group_id = group.get("id")
        for option in group.get("options", []):
            if not isinstance(option, dict) or not isinstance(option.get("id"), str):
                continue
            option_id = option["id"]
            option_ids.append(option_id)
            if option_id in option_to_group:
                errors.append(
                    f"equipment_options_1900.v1.json: option {option_id} appears in both "
                    f"{option_to_group[option_id]} and {group_id}"
                )
            else:
                option_to_group[option_id] = str(group_id)
    for duplicate in sorted(_duplicates(option_ids)):
        errors.append(f"equipment_options_1900.v1.json: duplicate option id {duplicate}")
    option_set = set(option_ids)

    model_doc = docs.get("vehicle_models_1900.v1.json", {})
    models = model_doc.get("models", []) if isinstance(model_doc, dict) else []
    model_ids = [x.get("id") for x in models if isinstance(x, dict) and isinstance(x.get("id"), str)]
    for duplicate in sorted(_duplicates(model_ids)):
        errors.append(f"vehicle_models_1900.v1.json: duplicate model id {duplicate}")
    model_set = set(model_ids)

    template_doc = docs.get("built_in_templates_1900.v1.json", {})
    templates = template_doc.get("templates", []) if isinstance(template_doc, dict) else []
    template_ids = [x.get("id") for x in templates if isinstance(x, dict) and isinstance(x.get("id"), str)]
    for duplicate in sorted(_duplicates(template_ids)):
        errors.append(f"built_in_templates_1900.v1.json: duplicate template id {duplicate}")
    template_set = set(template_ids)

    for index, model in enumerate(models):
        if not isinstance(model, dict):
            errors.append(f"vehicle_models_1900.v1.json.models[{index}]: expected object")
            continue
        location = f"vehicle_models_1900.v1.json:{model.get('id', index)}"
        if model.get("schema_version") != 1:
            errors.append(f"{location}: schema_version must be 1")
        manufacturer_id = model.get("manufacturer_id")
        if manufacturer_id not in manufacturer_set:
            errors.append(f"{location}: unknown manufacturer_id {manufacturer_id}")
        support_id = model.get("support_family_id")
        if support_id not in support_set:
            errors.append(f"{location}: unknown support_family_id {support_id}")
        profile_id = model.get("regional_market_profile_id")
        if profile_id not in profile_set:
            errors.append(f"{location}: unknown regional_market_profile_id {profile_id}")

        model_groups = model.get("equipment_group_ids", [])
        for group_id in model_groups:
            if group_id not in group_set:
                errors.append(f"{location}: unknown equipment group {group_id}")
        for template_id in model.get("built_in_template_ids", []):
            if template_id not in template_set:
                errors.append(f"{location}: unknown built-in template {template_id}")

        production = model.get("production", {})
        if isinstance(production, dict):
            for plant_id in production.get("factory_ids", []):
                if plant_id not in plant_ids:
                    errors.append(f"{location}: unknown factory/plant id {plant_id}")

        year = model.get("introduction_year")
        if not isinstance(year, int) or not (1800 <= year <= 2100):
            errors.append(f"{location}: invalid introduction_year {year!r}")
        platform = model.get("platform")
        if not isinstance(platform, dict):
            errors.append(f"{location}: missing platform object")
        else:
            speed = platform.get("max_speed_kph")
            if not isinstance(speed, (int, float)) or speed <= 0:
                errors.append(f"{location}: max_speed_kph must be positive")
            structural = platform.get("structural_speed_limit_kph")
            if isinstance(structural, (int, float)) and isinstance(speed, (int, float)) and speed > structural:
                errors.append(f"{location}: max_speed_kph exceeds structural_speed_limit_kph")
            for key in ("empty_mass_t", "service_mass_t", "payload_t", "cargo_volume_m3", "power_kw"):
                value = platform.get(key)
                if isinstance(value, (int, float)) and value < 0:
                    errors.append(f"{location}: {key} cannot be negative")

        provenance = model.get("provenance")
        if not isinstance(provenance, dict) or not provenance.get("source_urls"):
            errors.append(f"{location}: provenance source_urls required")
        else:
            for url in provenance.get("source_urls", []):
                if not isinstance(url, str) or not url.startswith(("https://", "http://")):
                    errors.append(f"{location}: invalid provenance URL {url!r}")

    template_model_counts = {model_id: 0 for model_id in model_set}
    for index, template in enumerate(templates):
        if not isinstance(template, dict):
            errors.append(f"built_in_templates_1900.v1.json.templates[{index}]: expected object")
            continue
        location = f"built_in_templates_1900.v1.json:{template.get('id', index)}"
        model_id = template.get("model_id")
        if model_id not in model_set:
            errors.append(f"{location}: unknown model_id {model_id}")
            continue
        template_model_counts[model_id] += 1
        model = next(x for x in models if isinstance(x, dict) and x.get("id") == model_id)
        allowed_groups = set(model.get("equipment_group_ids", []))
        for option_id in template.get("equipment_option_ids", []):
            if option_id not in option_set:
                errors.append(f"{location}: unknown equipment option {option_id}")
                continue
            option_group = option_to_group[option_id]
            if option_group not in allowed_groups:
                errors.append(
                    f"{location}: option {option_id} belongs to group {option_group}, "
                    f"which model {model_id} does not support"
                )

    for model_id, count in sorted(template_model_counts.items()):
        if count == 0:
            errors.append(f"vehicle model {model_id}: no built-in template")

    seed_doc = docs.get("opening_market_1900.v1.json", {})
    if isinstance(seed_doc, dict):
        for index, event in enumerate(seed_doc.get("factory_capability_events", [])):
            if isinstance(event, dict) and event.get("manufacturer_id") not in manufacturer_set:
                errors.append(
                    f"opening_market_1900.v1.json.factory_capability_events[{index}]: "
                    f"unknown manufacturer_id {event.get('manufacturer_id')}"
                )
        distribution = seed_doc.get("used_condition_distribution", {})
        if isinstance(distribution, dict):
            values = [
                distribution.get(key)
                for key in ("excellent", "good", "worn", "overhaul_due")
            ]
            if not all(isinstance(x, (int, float)) and x >= 0 for x in values):
                errors.append("opening_market_1900.v1.json: invalid used condition distribution")
            elif abs(sum(values) - 1.0) > 1e-9:
                errors.append("opening_market_1900.v1.json: used condition distribution must sum to 1")

    return VehicleContentResult(
        files=len(json_paths),
        manufacturers=len(manufacturer_set),
        support_families=len(support_set),
        market_profiles=len(profile_set),
        equipment_groups=len(group_set),
        equipment_options=len(option_set),
        templates=len(template_set),
        models=len(model_set),
        errors=tuple(errors),
    )


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    result = check_vehicle_content(root)
    for error in result.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    state = "FAIL" if result.errors else "PASS"
    print(
        f"{state}: {result.files} vehicle JSON files, "
        f"{result.manufacturers} manufacturers, {result.support_families} support families, "
        f"{result.market_profiles} market profiles, {result.equipment_groups} equipment groups, "
        f"{result.equipment_options} equipment options, {result.templates} templates, "
        f"{result.models} models; {len(result.errors)} errors. "
        "Content structure checks only; historical accuracy/art/game tests NOT RUN."
    )
    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
