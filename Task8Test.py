import unittest
from Task8 import Task8

class TestTask8(unittest.TestCase):
    def setUp(self):
        # Initialize Task8 object
        self.task8_instance = Task8()

    def test_func2(self):
        # Test func2 method
        with self.assertRaises(Exception):
            self.task8_instance.func2("UnitTest")

    def test_calculate_square(self):
        # Test calculate_square method
        square_result = self.task8_instance.calculate_square(5)
        expected_result = 25

        # Assert the result matches the expected result
        self.assertEqual(square_result, expected_result)

    def test_print_current_date(self):
        # Test print_current_date method
        with self.assertRaises(Exception):
            self.task8_instance.print_current_date()

if __name__ == "__main__":
    unittest.main()
