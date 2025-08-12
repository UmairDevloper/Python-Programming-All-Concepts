try:
    with (
        open("1.txt", "r") as file1,
        open("2.txt", "r") as file2,
        open("3.txt", "r") as file3,
    ):
        print(file1.read())
        print(file2.read())
        print(file3.read())

except FileNotFoundError as error:
    print("File not found", error )