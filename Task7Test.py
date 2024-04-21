import unittest
from Task7 import Task7

class TestTask7(unittest.TestCase):
    def setUp(self):
        # Initialize Task7 object
        self.task7_instance = Task7()

    def test_func1(self):
        # Test func1 method
        with self.assertRaises(Exception):
            self.task7_instance.func1("UnitTest")

    def test_print_python_version(self):
        # Test print_python_version method
        with self.assertRaises(Exception):
            self.task7_instance.print_python_version("UnitTest")

    def test_process_parameters(self):
        # Test process_parameters method
        result_dict = self.task7_instance.process_parameters(10, 3.14, "tag1 value1", "tag2 value2", "tag3 value3")
        expected_result = {'tag1': 'value1', 'tag2': 'value2', 'tag3': 'value3'}

        # Assert the result matches the expected result
        self.assertEqual(result_dict, expected_result)

if __name__ == "__main__":
    unittest.main()
