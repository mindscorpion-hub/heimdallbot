from functions.write_file import write_file

def tests():
    print("First Test:")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print("Second Test:")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print("Third Test:")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

tests()