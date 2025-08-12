
n = int(input("Enter a number: "))

with open("table.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{n} * {i} = {n * i}\n")