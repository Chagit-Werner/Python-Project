import pandas as pd;
class FileOperation:
    #---------------------------------------1
    def read_excel(self, file_path: str):
        data = pd.read_csv(file_path)
        return data;


    #---------------------------------------2
    def save_to_excel(self, data, file_name: str):
        try:
             print(data)
             df = pd.DataFrame(data)
             print(df)
             df.to_csv(file_name, index=False, mode='w')
        except Exception as e:
            print(f"Error saving data to CSV file: {e}")



            #בשביל לבדוק שהפונקציות עובדות ניסיתי אותן:------------------------------------


data = {
    'Name': ['Alice','Alice', 'Bob', 'Charlie'],
    'Age': [25,25, 30, 35],
    'City': ['New York','New York', 'San Francisco', 'Los Angeles']
}
file_operator = FileOperation()
file_operator.save_to_excel(data, "output_file.csv")


excel_data = file_operator.read_excel(r"C:\Users\user1\OneDrive\Desktop\YafeNof.csv")

if excel_data is not None:
    print(excel_data)
from SalesData import SalesData


