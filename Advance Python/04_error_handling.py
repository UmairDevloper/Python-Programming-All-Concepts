a = int(input("Enter a number: "))
b = int(input("Enter another number: "))


if(b == 0):
    raise ZeroDivisionError ("Can't divide by zero")
else:
    print(a/b)