"""Validate observable dialogue-to-shot links using public and synthetic data."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("repository_validator", ROOT / "scripts/validate_repository.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class VisualPlanLinkTests(unittest.TestCase):
    def setUp(self):
        self.plan = {"shots": [{"id": "S1", "spoken_line_ids": ["L1", "L2"]}]}
        self.dialogue = {"lines": [{"id": "L1", "text": "First fact."},
                                   {"id": "L2", "text": "Second fact."}]}

    def check_links(self, plan, dialogue):
        with tempfile.TemporaryDirectory(prefix="teaching-links-test-") as tmp:
            root = Path(tmp)
            example = root / "examples" / "synthetic"
            example.mkdir(parents=True)
            (example / "visual-plan.json").write_text(json.dumps(plan), encoding="utf-8")
            (example / "dialogue.json").write_text(json.dumps(dialogue), encoding="utf-8")
            errors = []
            with patch.object(validator, "ROOT", root):
                validator.validate_visual_plan_links(errors)
            return errors

    def test_public_examples_keep_passing(self):
        for path in sorted((ROOT / "examples").glob("*/visual-plan.json")):
            with self.subTest(example=path.parent.name):
                plan = json.loads(path.read_text(encoding="utf-8"))
                dialogue = json.loads(path.with_name("dialogue.json").read_text(encoding="utf-8"))
                self.assertEqual(self.check_links(plan, dialogue), [])

    def test_one_line_can_support_multiple_shots(self):
        self.plan["shots"].append({"id": "S2", "spoken_line_ids": ["L1"]})
        self.assertEqual(self.check_links(self.plan, self.dialogue), [])

    def test_duplicate_dialogue_ids_are_rejected(self):
        self.dialogue["lines"].append({"id": "L1", "text": "A different untracked sentence."})
        self.assertTrue(self.check_links(self.plan, self.dialogue))

    def test_missing_or_non_array_lines_are_rejected(self):
        for dialogue in ({}, None, [], "invalid", {"lines": None}, {"lines": {}}, {"lines": "L1"}):
            with self.subTest(dialogue=dialogue):
                self.assertTrue(self.check_links(self.plan, dialogue))

    def test_non_object_lines_are_not_silently_discarded(self):
        for line in (None, [], "untracked sentence", 3):
            with self.subTest(line=line):
                dialogue = deepcopy(self.dialogue)
                dialogue["lines"].append(line)
                self.assertTrue(self.check_links(self.plan, dialogue))

    def test_missing_or_invalid_line_ids_are_rejected(self):
        for line in ({"text": "Missing ID"}, {"id": None}, {"id": 1},
                     {"id": True}, {"id": []}, {"id": ""}, {"id": " "}):
            with self.subTest(line=line):
                dialogue = deepcopy(self.dialogue)
                dialogue["lines"].append(line)
                self.assertTrue(self.check_links(self.plan, dialogue))

    def test_unknown_line_reference_is_rejected(self):
        self.plan["shots"][0]["spoken_line_ids"].append("L99")
        self.assertTrue(self.check_links(self.plan, self.dialogue))

    def test_uncovered_line_is_rejected(self):
        self.dialogue["lines"].append({"id": "L3", "text": "Uncovered."})
        self.assertTrue(self.check_links(self.plan, self.dialogue))

    def test_duplicate_shot_id_is_rejected(self):
        self.plan["shots"].append(deepcopy(self.plan["shots"][0]))
        self.assertTrue(self.check_links(self.plan, self.dialogue))

    def test_empty_dialogue_lines_are_rejected(self):
        self.assertTrue(self.check_links(self.plan, {"lines": []}))


if __name__ == "__main__":
    unittest.main()
