
with open('log.txt') as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("Python" in line):
        print(f"The word python is in the file on line {lineno}")
        break
    lineno += 1

else:
        print(f"The word python is not in the file on line {lineno}")