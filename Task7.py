import datetime
from abc import ABC, abstractmethod
import sys
"""
חשוב לי להסביר: מחלקת SalesData שלי הייתה נראית לי מעט מפולגנת,
לא רציתי להכביד עליה בפונקציות נו ספות ולכן פתחתי מחלקות שונות בדפים שונים למשימוצ 7-8-9
תודה רבה.!!!
"""
class Task7:
    #1
    def func1(self, name):
        try:
            print("Hello!!!")
        except Exception as ex:
            print(f"<{name}> {datetime.datetime.now()} Error type: {str(ex)} <{name}>")
    #4
    def print_python_version(self, name):
        try:
             print(f"Python Version: {sys.version}")
        except Exception as e:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"<{name}> {datetime.datetime.now()} Error type: {str(e)} <{name}>")

   #5:
    def process_parameters(*args, **kwargs):
        result_dict = {}

        for arg in args:
            if isinstance(arg, (int, float)):
                print(f"Numeric value: {arg}")
            elif isinstance(arg, str):
                tag, value = arg.split()
                result_dict[tag] = value

        return result_dict
 #2
#בפיתון כידוע אין ממשקים!!!
class FileReader(ABC):
    @abstractmethod
    def read_file(self, file_path: str):
        pass
    #שאלה 3 במשימה 7 משולבת במחלקת :SalesData
    #שאלות 7 - 6 במשימה 7 אף היא משולבת במחלקת SalesData

