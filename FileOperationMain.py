from FileOperation import FileOperation


if __name__ == "__main__":
    data = {
        'Name': ['Alice', 'Alice', 'Bob', 'Charlie'],
        'Age': [25, 25, 30, 35],
        'City': ['New York', 'New York', 'San Francisco', 'Los Angeles']
    }

    file_operator = FileOperation()
    file_operator.save_to_excel(data, "output_file.csv")

    excel_data = file_operator.read_excel("output_file.csv")

    if excel_data is not None:
        print(excel_data)
