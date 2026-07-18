"""Unit tests for the Vision_Merchandising tier: totals(), report()."""

import inspect
import unittest

from tests._loader import load_marker

totals = load_marker("sales", "Vision_Merchandising/sales.py").totals
report = load_marker("report", "Vision_Merchandising/build/report.py").report

NON_LEAK_SUFFIX = "(proves no cross-submodule leak)"


class TestVisionMerchandising(unittest.TestCase):
    def test_totals_returns_marker(self):
        self.assertEqual(totals(), "vision-merchandising: always included")

    def test_totals_returns_str(self):
        self.assertIsInstance(totals(), str)

    def test_totals_non_empty(self):
        self.assertNotEqual(totals(), "")

    def test_totals_is_deterministic(self):
        self.assertEqual(totals(), totals())

    def test_totals_zero_arg_signature(self):
        self.assertEqual(len(inspect.signature(totals).parameters), 0)

    def test_report_returns_marker(self):
        self.assertEqual(
            report(),
            "vision-merchandising/build: included (proves no cross-submodule leak)",
        )

    def test_report_returns_str(self):
        self.assertIsInstance(report(), str)

    def test_report_non_empty(self):
        self.assertNotEqual(report(), "")

    def test_report_is_deterministic(self):
        self.assertEqual(report(), report())

    def test_report_zero_arg_signature(self):
        self.assertEqual(len(inspect.signature(report).parameters), 0)

    def test_report_non_leak_suffix(self):
        self.assertTrue(report().endswith(NON_LEAK_SUFFIX))


if __name__ == "__main__":
    unittest.main()
