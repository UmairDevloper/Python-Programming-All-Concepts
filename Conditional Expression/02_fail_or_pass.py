
marks = []

for i in range(3):
    marks.append(int(input("Enter marks: ")))

if marks[0] > 33 and marks[1] > 33:
    if marks[2] > 33:
        print("Pass")
    else:
        print("Fail")
else:
    print("Fail")