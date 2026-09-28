"""Tests for the Tavern Ledger. Run with: python -m unittest -v"""

import unittest

import tavern


class TavernTests(unittest.TestCase):
    def test_add_new_item(self):
        data = {}
        tavern.add(data, "ale", 5, 2.0)
        self.assertEqual(data["ale"], {"qty": 5, "price": 2.0})

    def test_total(self):
        data = {"ale": {"qty": 2, "price": 2.0}, "mead": {"qty": 1, "price": 5.5}}
        self.assertEqual(tavern.total(data), 9.5)


if __name__ == "__main__":
    unittest.main()
