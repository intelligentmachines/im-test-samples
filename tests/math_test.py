import unittest
from src.math import MathUtils


class MathUtilsTestSuit(unittest.TestCase):

    def test_divide_check(self):
        a = 1
        b = 2

        self.assertEqual(MathUtils.divide(a, b), 0.5)

    def test_if_divide_output_is_float(self):
        a = 1
        b = 2
        output = MathUtils.divide(a, b)  # 0.5

        self.assertIsInstance(output, float)  # 1, 2, 3

    def test_number_even(self):
        a = 2
        self.assertTrue(MathUtils.is_even(a))

        # assert MathUtils.is_even(a) == True

    def test_number_odd(self):
        a = 5
        self.assertFalse(MathUtils.is_even(a))

        # assert MathUtils.is_even(a) == True

    def test_if_is_even_output_is_boolean(self):
        a = 5
        output = MathUtils.is_even(a)
        self.assertIsInstance(output, bool)

        # assert MathUtils.is_even(a) == True



