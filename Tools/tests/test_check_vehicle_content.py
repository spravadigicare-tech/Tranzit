"""Self-tests for the vehicle-content validator."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_vehicle_content import check_vehicle_content


class VehicleContentValidatorTests(unittest.TestCase):
    def fixture(self):
        directory = tempfile.TemporaryDirectory()
        root = Path(directory.name)
        base = root / "content" / "vehicles"
        base.mkdir(parents=True)
        (base / "vehicle_model.schema.v1.json").write_text("{}\n", encoding="utf-8")
        docs = {
            "manufacturers.v1.json": {
                "manufacturers": [{"id": "m", "plant_ids": ["p"]}]
            },
            "support_families.v1.json": {
                "support_families": [{"id": "s"}]
            },
            "regional_market_profiles.v1.json": {
                "profiles": [{"id": "r"}]
            },
            "production_input_groups.v1.json": {
                "recipes": [{"id": "recipe"}]
            },
            "equipment_options_1900.v1.json": {
                "groups": [{"id": "g", "options": [{"id": "o"}]}]
            },
            "built_in_templates_1900.v1.json": {
                "templates": [{"id": "t", "model_id": "v", "equipment_option_ids": ["o"]}]
            },
            "vehicle_models_1900.v1.json": {
                "models": [{
                    "schema_version": 1,
                    "id": "v",
                    "introduction_year": 1900,
                    "manufacturer_id": "m",
                    "support_family_id": "s",
                    "regional_market_profile_id": "r",
                    "equipment_group_ids": ["g"],
                    "built_in_template_ids": ["t"],
                    "platform": {"max_speed_kph": 10, "structural_speed_limit_kph": 10},
                    "production": {"factory_ids": ["p"], "material_recipe_id": "recipe"},
                    "provenance": {"source_urls": ["https://example.invalid"]}
                }]
            },
            "opening_market_1900.v1.json": {
                "factory_capability_events": [{"manufacturer_id": "m"}],
                "used_condition_distribution": {
                    "excellent": 0.1, "good": 0.45, "worn": 0.35, "overhaul_due": 0.1
                }
            },
            "equipment_options_1901_1919.v1.json": {"groups": []},
            "equipment_options_1920_1959.v1.json": {"groups": []},
            "equipment_options_1960_1989.v1.json": {"groups": []},
            "equipment_options_1990_2026.v1.json": {"groups": []},
            "built_in_templates_1901_1919.v1.json": {"templates": []},
            "built_in_templates_1920_1959.v1.json": {"templates": []},
            "built_in_templates_1960_1989.v1.json": {"templates": []},
            "built_in_templates_1990_2026.v1.json": {"templates": []},
            "vehicle_models_1901_1919.v1.json": {"models": []},
            "vehicle_models_1920_1959.v1.json": {"models": []},
            "vehicle_models_1960_1989.v1.json": {"models": []},
            "vehicle_models_1990_2026.v1.json": {"models": []},
        }
        for name, data in docs.items():
            (base / name).write_text(json.dumps(data), encoding="utf-8")
        return directory, root, base

    def test_valid_minimal_fixture(self):
        directory, root, _ = self.fixture()
        with directory:
            self.assertEqual(check_vehicle_content(root).errors, ())

    def test_unknown_reference_rejected(self):
        directory, root, base = self.fixture()
        with directory:
            path = base / "vehicle_models_1900.v1.json"
            data = json.loads(path.read_text())
            data["models"][0]["support_family_id"] = "missing"
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertTrue(any("unknown support_family_id" in x for x in check_vehicle_content(root).errors))

    def test_available_until_rejected_anywhere(self):
        directory, root, base = self.fixture()
        with directory:
            path = base / "vehicle_models_1900.v1.json"
            data = json.loads(path.read_text())
            data["models"][0]["available_until"] = 1910
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertTrue(any("forbidden hard availability gate" in x for x in check_vehicle_content(root).errors))

    def test_template_option_must_belong_to_model_group(self):
        directory, root, base = self.fixture()
        with directory:
            path = base / "equipment_options_1900.v1.json"
            data = json.loads(path.read_text())
            data["groups"].append({"id": "other", "options": [{"id": "wrong"}]})
            path.write_text(json.dumps(data), encoding="utf-8")
            path = base / "built_in_templates_1900.v1.json"
            data = json.loads(path.read_text())
            data["templates"][0]["equipment_option_ids"] = ["wrong"]
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertTrue(any("does not support" in x for x in check_vehicle_content(root).errors))

    def test_material_recipe_required(self):
        directory, root, base = self.fixture()
        with directory:
            path = base / "vehicle_models_1900.v1.json"
            data = json.loads(path.read_text())
            del data["models"][0]["production"]["material_recipe_id"]
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertTrue(any("material_recipe_id" in x for x in check_vehicle_content(root).errors))

    def test_condition_distribution_must_sum_to_one(self):
        directory, root, base = self.fixture()
        with directory:
            path = base / "opening_market_1900.v1.json"
            data = json.loads(path.read_text())
            data["used_condition_distribution"]["good"] = 0.2
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertTrue(any("must sum to 1" in x for x in check_vehicle_content(root).errors))


if __name__ == "__main__":
    unittest.main()
