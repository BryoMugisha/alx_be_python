# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ----------- ADD TESTS -----------
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -7), -10)

    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(-2, 8), 6)

    # ----------- SUBTRACT TESTS -----------
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_to_negative(self):
        self.assertEqual(self.calc.subtract(3, 8), -5)

    # ----------- MULTIPLY TESTS -----------
    def test_multiply_numbers(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)

    # ----------- DIVIDE TESTS -----------
    def test_divide_numbers(self):
        self.assertEqual(self.calc.divide(20, 5), 4)

    def test_divide_fraction(self):
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
