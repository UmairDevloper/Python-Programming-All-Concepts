num = int(input("Enter the number: "))

def print_pattern(num):
    i = num
    while i > 0:
        for j in range(0, i):
            print("*", end=" ")
        print("\r")
        i -= 1

print_pattern(num)