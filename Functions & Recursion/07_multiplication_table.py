
num = int(input("Enter the number:"))

def multiplication_table(num):
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i)

multiplication_table(num)