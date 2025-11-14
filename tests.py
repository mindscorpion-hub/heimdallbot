from functions.run_python_file import run_python_file

def tests():
    print("First Test:")
    print(run_python_file("calculator", "main.py"))

    print("Second Test:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("Third Test:")
    print(run_python_file("calculator", "tests.py"))

    print("Fourth Test:")
    print(run_python_file("calculator", "../main.py"))

    print("Fifth Test:")
    print(run_python_file("calculator", "nonexistent.py"))

    print("Sixth Test:")
    print(run_python_file("calculator", "lorem.txt"))

tests()