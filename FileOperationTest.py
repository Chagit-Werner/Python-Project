import unittest
import pandas as pd
from FileOperation import FileOperation

class TestFileOperation(unittest.TestCase):
    def setUp(self):
        # Initialize FileOperation object
        self.file_operation_instance = FileOperation()

    def test_read_excel(self):
        # Test read_excel method
        file_path = "path/to/your/excel_file.csv"  # Provide an actual file path
        result = self.file_operation_instance.read_excel(file_path)

        # Assert the result is not None
        self.assertIsNotNone(result)

    def test_save_to_excel(self):
        # Test save_to_excel method
        # Assuming there is some data to save (you may need to modify this)
        data_to_save = {'Name': ['Alice', 'Bob'], 'Age': [25, 30], 'City': ['New York', 'San Francisco']}
        file_name = "output_file.csv"
        self.file_operation_instance.save_to_excel(data_to_save, file_name)

        # Read the saved file and check if it exists
        saved_data = pd.read_csv(file_name)

        # Assert the saved data is not None
        self.assertIsNotNone(saved_data)



if __name__ == "__main__":
    unittest.main()
