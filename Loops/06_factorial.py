
num = int(input("Enter a number: "))

ans = 1
i = num

while i >= 1:
    ans *= i
    i -= 1

print(ans)