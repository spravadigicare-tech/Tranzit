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


VALID_VEHICLE_KINDS_BY_MODE = {
    "rail": {
        "locomotive",
        "railcar",
        "emu",
        "dmu",
        "passenger_coach",
        "passenger_coach_set",
        "service_coach",
        "freight_wagon",
    },
    "road": {"truck", "bus", "horse_freight", "horse_bus"},
}


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
        "production_input_groups.v1.json",
        "factory_capability_policies.v1.json",
        "import_route_profiles.v1.json",
        "equipment_options_1900.v1.json",
        "built_in_templates_1900.v1.json",
        "vehicle_models_1900.v1.json",
        "vehicle_models_1901_1919.v1.json",
        "vehicle_models_1920_1959.v1.json",
        "vehicle_models_1960_1989.v1.json",
        "vehicle_models_1990_2026.v1.json",
        "built_in_templates_1901_1919.v1.json",
        "built_in_templates_1920_1959.v1.json",
        "built_in_templates_1960_1989.v1.json",
        "built_in_templates_1990_2026.v1.json",
        "equipment_options_1901_1919.v1.json",
        "equipment_options_1920_1959.v1.json",
        "equipment_options_1960_1989.v1.json",
        "equipment_options_1990_2026.v1.json",
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

    production_input_doc = docs.get("production_input_groups.v1.json", {})
    production_recipes = production_input_doc.get("recipes", []) if isinstance(production_input_doc, dict) else []
    production_recipe_ids = [
        x.get("id")
        for x in production_recipes
        if isinstance(x, dict) and isinstance(x.get("id"), str)
    ]
    for duplicate in sorted(_duplicates(production_recipe_ids)):
        errors.append(f"production_input_groups.v1.json: duplicate recipe id {duplicate}")
    production_recipe_set = set(production_recipe_ids)

    capability_doc = docs.get("factory_capability_policies.v1.json", {})
    capability_states = set(capability_doc.get("states", [])) if isinstance(capability_doc, dict) else set()
    capability_policies = capability_doc.get("policies", []) if isinstance(capability_doc, dict) else []
    capability_policy_ids = [
        x.get("id")
        for x in capability_policies
        if isinstance(x, dict) and isinstance(x.get("id"), str)
    ]
    for duplicate in sorted(_duplicates(capability_policy_ids)):
        errors.append(f"factory_capability_policies.v1.json: duplicate policy id {duplicate}")
    capability_policy_set = set(capability_policy_ids)

    import_routes_doc = docs.get("import_route_profiles.v1.json", {})
    import_routes = import_routes_doc.get("profiles", []) if isinstance(import_routes_doc, dict) else []
    import_route_ids = [
        x.get("id")
        for x in import_routes
        if isinstance(x, dict) and isinstance(x.get("id"), str)
    ]
    for duplicate in sorted(_duplicates(import_route_ids)):
        errors.append(f"import_route_profiles.v1.json: duplicate route profile id {duplicate}")

    equipment_sources: list[tuple[str, dict[str, Any]]] = []
    for name, document in docs.items():
        if name.startswith("equipment_options_") and name.endswith(".v1.json") and isinstance(document, dict):
            equipment_sources.append((name, document))
    groups: list[dict[str, Any]] = []
    group_source: dict[str, str] = {}
    option_to_group: dict[str, str] = {}
    option_source: dict[str, str] = {}
    group_ids: list[str] = []
    option_ids: list[str] = []
    for name, equipment_doc in sorted(equipment_sources):
        for group in equipment_doc.get("groups", []):
            if not isinstance(group, dict) or not isinstance(group.get("id"), str):
                continue
            group_id = group["id"]
            groups.append(group)
            group_ids.append(group_id)
            if group_id in group_source:
                errors.append(f"{name}: duplicate equipment group id {group_id} also defined in {group_source[group_id]}")
            else:
                group_source[group_id] = name
            for option in group.get("options", []):
                if not isinstance(option, dict) or not isinstance(option.get("id"), str):
                    continue
                option_id = option["id"]
                option_ids.append(option_id)
                if option_id in option_to_group:
                    errors.append(
                        f"{name}: option {option_id} appears in both "
                        f"{option_to_group[option_id]} and {group_id}"
                    )
                else:
                    option_to_group[option_id] = group_id
                    option_source[option_id] = name
    group_set = set(group_ids)
    option_set = set(option_ids)

    model_sources: list[tuple[str, dict[str, Any]]] = []
    models: list[dict[str, Any]] = []
    model_source: dict[str, str] = {}
    model_ids: list[str] = []
    for name, document in docs.items():
        if name.startswith("vehicle_models_") and name.endswith(".v1.json") and isinstance(document, dict):
            model_sources.append((name, document))
    for name, model_doc in sorted(model_sources):
        for model in model_doc.get("models", []):
            if not isinstance(model, dict) or not isinstance(model.get("id"), str):
                continue
            model_id = model["id"]
            models.append(model)
            model_ids.append(model_id)
            if model_id in model_source:
                errors.append(f"{name}: duplicate model id {model_id} also defined in {model_source[model_id]}")
            else:
                model_source[model_id] = name
    model_set = set(model_ids)

    template_sources: list[tuple[str, dict[str, Any]]] = []
    templates: list[dict[str, Any]] = []
    template_source: dict[str, str] = {}
    template_ids: list[str] = []
    for name, document in docs.items():
        if name.startswith("built_in_templates_") and name.endswith(".v1.json") and isinstance(document, dict):
            template_sources.append((name, document))
    for name, template_doc in sorted(template_sources):
        for template in template_doc.get("templates", []):
            if not isinstance(template, dict) or not isinstance(template.get("id"), str):
                continue
            template_id = template["id"]
            templates.append(template)
            template_ids.append(template_id)
            if template_id in template_source:
                errors.append(f"{name}: duplicate template id {template_id} also defined in {template_source[template_id]}")
            else:
                template_source[template_id] = name
    template_set = set(template_ids)

    for index, model in enumerate(models):
        if not isinstance(model, dict):
            errors.append(f"vehicle_models_*.v1.json.models[{index}]: expected object")
            continue
        model_id = model.get("id")
        source_name = model_source.get(str(model_id), "vehicle_models_*.v1.json")
        location = f"{source_name}:{model_id if model_id is not None else index}"
        if model.get("schema_version") != 1:
            errors.append(f"{location}: schema_version must be 1")
        mode = model.get("mode")
        vehicle_kind = model.get("vehicle_kind")
        if mode not in VALID_VEHICLE_KINDS_BY_MODE:
            errors.append(f"{location}: unknown or missing mode {mode!r}")
        elif vehicle_kind not in VALID_VEHICLE_KINDS_BY_MODE[mode]:
            errors.append(
                f"{location}: vehicle_kind {vehicle_kind!r} is invalid for mode {mode!r}"
            )
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
            material_recipe_id = production.get("material_recipe_id")
            if material_recipe_id not in production_recipe_set:
                errors.append(f"{location}: unknown or missing material_recipe_id {material_recipe_id}")
            capability_policy_id = production.get("capability_policy_id")
            if capability_policy_id not in capability_policy_set:
                errors.append(f"{location}: unknown or missing capability_policy_id {capability_policy_id}")
            base_cost_index = production.get("base_cost_index")
            if not isinstance(base_cost_index, (int, float)) or base_cost_index < 0:
                errors.append(f"{location}: production.base_cost_index must be a non-negative number")
            capability_state = production.get("initial_capability_state")
            if capability_state not in capability_states:
                errors.append(f"{location}: unknown or missing initial_capability_state {capability_state}")
        else:
            errors.append(f"{location}: missing production object")

        maintenance = model.get("maintenance_profile")
        if not isinstance(maintenance, dict) or not maintenance:
            errors.append(f"{location}: non-empty maintenance_profile required")

        consumption = model.get("consumption_profile")
        if not isinstance(consumption, dict) or not isinstance(consumption.get("type"), str):
            errors.append(f"{location}: consumption_profile.type required")

        year = model.get("introduction_year")
        if not isinstance(year, int) or not (1800 <= year <= 2100):
            errors.append(f"{location}: invalid introduction_year {year!r}")
        platform = model.get("platform")
        if not isinstance(platform, dict):
            errors.append(f"{location}: missing platform object")
        else:
            if "empty_mass_t" not in platform:
                errors.append(
                    f"{location}: platform.empty_mass_t key required; use null only when the value is explicitly unresolved"
                )
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
            errors.append(f"built_in_templates_*.v1.json.templates[{index}]: expected object")
            continue
        template_id = template.get("id")
        source_name = template_source.get(str(template_id), "built_in_templates_*.v1.json")
        location = f"{source_name}:{template_id if template_id is not None else index}"
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

    opening_models_doc = docs.get("vehicle_models_1900.v1.json", {})
    if isinstance(opening_models_doc, dict) and opening_models_doc.get("scope") == "1900 opening vehicle families":
        opening_models = [x for x in opening_models_doc.get("models", []) if isinstance(x, dict)]

        def _opening_count(predicate) -> int:
            return sum(1 for model in opening_models if predicate(model))

        opening_requirements = [
            (
                "steam locomotives",
                4,
                _opening_count(
                    lambda model: model.get("vehicle_kind") == "locomotive"
                    and str(model.get("support_family_id", "")).startswith("rail_steam")
                ),
            ),
            (
                "freight rolling stock",
                6,
                _opening_count(lambda model: model.get("vehicle_kind") == "freight_wagon"),
            ),
            (
                "passenger/service rolling stock",
                4,
                _opening_count(
                    lambda model: model.get("vehicle_kind") in {"passenger_coach", "service_coach"}
                ),
            ),
            (
                "road freight",
                4,
                _opening_count(
                    lambda model: model.get("mode") == "road"
                    and model.get("vehicle_kind") in {"horse_freight", "truck"}
                ),
            ),
            (
                "road passenger",
                2,
                _opening_count(
                    lambda model: model.get("mode") == "road"
                    and model.get("vehicle_kind") in {"horse_bus", "bus"}
                ),
            ),
        ]
        for label, minimum, actual in opening_requirements:
            if actual < minimum:
                errors.append(
                    f"vehicle_models_1900.v1.json: opening {label} coverage {actual} "
                    f"is below required minimum {minimum}"
                )

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
