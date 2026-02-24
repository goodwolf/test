import unittest
from pi_calculator import calculate_pi


class TestCalculatePi(unittest.TestCase):
    def test_pi_rounded_to_two_decimal_places(self):
        """Pi rounded to 2 decimal places should equal 3.14."""
        self.assertEqual(calculate_pi(), 3.14)

    def test_pi_is_float(self):
        """The result should be a float."""
        self.assertIsInstance(calculate_pi(), float)

    def test_pi_default_is_two_decimal_places(self):
        """Default argument should produce a value with at most 2 decimal places."""
        result = calculate_pi()
        result_str = str(result)
        decimal_part = result_str.split(".")[1] if "." in result_str else ""
        self.assertLessEqual(len(decimal_part), 2)

    def test_pi_value_between_three_and_four(self):
        """Pi to 2 decimal places should still be between 3 and 4."""
        result = calculate_pi()
        self.assertGreater(result, 3)
        self.assertLess(result, 4)

    def test_pi_explicit_two_decimal_places(self):
        """Explicitly passing decimal_places=2 should equal 3.14."""
        self.assertEqual(calculate_pi(decimal_places=2), 3.14)


if __name__ == "__main__":
    unittest.main()
