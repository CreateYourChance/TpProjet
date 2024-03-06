from app import add
import unittest


class TestAddition(unittest.TestCase):
    def test_deux_zero(self):
        self.assertEqual(add(0, 0), 0, "0 + 0 = 0")

    def test_decimaux(self):
        self.assertEqual(add(6.1, 4.7), 10.8)

    def test_negatifs(self):
        self.assertAlmostEqual(add(5, 0.1), 5.1)

    def test_entiers(self):
        self.assertEqual(add(5, 7), 12)