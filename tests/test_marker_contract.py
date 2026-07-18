"""Cross-cutting, parametrized contract tests over all six marker functions."""

import inspect
import unittest

from tests._loader import load_marker

MARKERS = [
    ("app", "app.py", "main", "root: always included"),
    ("service", "Vision_CENTRAL/service.py", "run", "vision-central: always included"),
    ("util", "Vision_CENTRAL/nested-utils/util.py", "helper", "nested-utils: always included"),
    (
        "generated",
        "Vision_CENTRAL/nested-utils/build/generated.py",
        "generated",
        "nested-utils/build: included (proves no cross-submodule leak)",
    ),
    ("sales", "Vision_Merchandising/sales.py", "totals", "vision-merchandising: always included"),
    (
        "report",
        "Vision_Merchandising/build/report.py",
        "report",
        "vision-merchandising/build: included (proves no cross-submodule leak)",
    ),
]


def _load(name, rel_path, function):
    return getattr(load_marker(name, rel_path), function)


class TestMarkerContract(unittest.TestCase):
    def test_exact_values(self):
        for name, rel_path, function, expected in MARKERS:
            with self.subTest(marker=name):
                self.assertEqual(_load(name, rel_path, function)(), expected)

    def test_returns_str(self):
        for name, rel_path, function, _expected in MARKERS:
            with self.subTest(marker=name):
                self.assertIsInstance(_load(name, rel_path, function)(), str)

    def test_non_empty(self):
        for name, rel_path, function, _expected in MARKERS:
            with self.subTest(marker=name):
                self.assertNotEqual(_load(name, rel_path, function)(), "")

    def test_deterministic(self):
        for name, rel_path, function, _expected in MARKERS:
            with self.subTest(marker=name):
                fn = _load(name, rel_path, function)
                self.assertEqual(fn(), fn())

    def test_zero_arg_signature(self):
        for name, rel_path, function, _expected in MARKERS:
            with self.subTest(marker=name):
                fn = _load(name, rel_path, function)
                self.assertEqual(len(inspect.signature(fn).parameters), 0)


if __name__ == "__main__":
    unittest.main()
