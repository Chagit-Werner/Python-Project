from task8 import Task8

def main():
    # Create an instance of Task8
    task8_instance = Task8()

    # Test func2 method
    task8_instance.func2("Main")

    # Test calculate_square method
    square_result = task8_instance.calculate_square(5)
    print("Square Result:", square_result)

    # Test print_current_date method
    task8_instance.print_current_date()

if __name__ == "__main__":
    main()
