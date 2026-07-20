"""Unit tests for the Vision_CENTRAL tier: run(), helper(), generated()."""

import inspect
import unittest

from tests._loader import load_marker

run = load_marker("service", "Vision_CENTRAL/service.py").run
helper = load_marker("util", "Vision_CENTRAL/nested-utils/util.py").helper
generated = load_marker(
    "generated", "Vision_CENTRAL/nested-utils/build/generated.py"
).generated

NON_LEAK_SUFFIX = "(proves no cross-submodule leak)"


class TestVisionCentral(unittest.TestCase):
    def test_run_returns_marker(self):
        self.assertEqual(run(), "vision-central: always included")

    def test_run_returns_str(self):
        self.assertIsInstance(run(), str)

    def test_run_non_empty(self):
        self.assertNotEqual(run(), "")

    def test_run_is_deterministic(self):
        self.assertEqual(run(), run())

    def test_run_zero_arg_signature(self):
        self.assertEqual(len(inspect.signature(run).parameters), 0)

    def test_helper_returns_marker(self):
        self.assertEqual(helper(), "nested-utils: always included")

    def test_helper_returns_str(self):
        self.assertIsInstance(helper(), str)

    def test_helper_non_empty(self):
        self.assertNotEqual(helper(), "")

    def test_helper_is_deterministic(self):
        self.assertEqual(helper(), helper())

    def test_helper_zero_arg_signature(self):
        self.assertEqual(len(inspect.signature(helper).parameters), 0)

    def test_generated_returns_marker(self):
        self.assertEqual(
            generated(),
            "nested-utils/build: included (proves no cross-submodule leak)",
        )

    def test_generated_returns_str(self):
        self.assertIsInstance(generated(), str)

    def test_generated_non_empty(self):
        self.assertNotEqual(generated(), "")

    def test_generated_is_deterministic(self):
        self.assertEqual(generated(), generated())

    def test_generated_zero_arg_signature(self):
        self.assertEqual(len(inspect.signature(generated).parameters), 0)

    def test_generated_non_leak_suffix(self):
        self.assertTrue(generated().endswith(NON_LEAK_SUFFIX))


if __name__ == "__main__":
    unittest.main()
