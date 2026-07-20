"""Unit tests for the root-tier marker: app.py::main()."""

import inspect
import unittest

from tests._loader import load_marker

main = load_marker("app", "app.py").main
EXPECTED = "root: always included"


class TestRootMarkers(unittest.TestCase):
    def test_main_returns_marker(self):
        self.assertEqual(main(), EXPECTED)

    def test_main_returns_str(self):
        self.assertIsInstance(main(), str)

    def test_main_non_empty(self):
        self.assertNotEqual(main(), "")

    def test_main_is_deterministic(self):
        self.assertEqual(main(), main())

    def test_main_zero_arg_signature(self):
        self.assertEqual(len(inspect.signature(main).parameters), 0)


if __name__ == "__main__":
    unittest.main()
