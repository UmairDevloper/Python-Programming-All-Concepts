with open('this.txt', 'r') as f1:
    content1 = f1.read()
with open('this_copy.txt', 'r') as f2:
    content2 = f2.read()
if(content1 == content2):
    print("The content of both files are same.")
else:
    print("The content of both files are different.")