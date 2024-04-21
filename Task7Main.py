from Task7 import Task7

def main():
    # Create an instance of Task7
    task7_instance = Task7()

    # Test func1 method
    task7_instance.func1("Main")

    # Test print_python_version method
    task7_instance.print_python_version("Main")

    # Test process_parameters method
    result_dict = task7_instance.process_parameters(10, 3.14, "tag1 value1", "tag2 value2", "tag3 value3")
    print("Result Dictionary:")
    print(result_dict)

if __name__ == "__main__":
    main()
