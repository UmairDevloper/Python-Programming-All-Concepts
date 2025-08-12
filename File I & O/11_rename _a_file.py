with open('this_copy.txt', 'r') as f:
    content = f.read()
with open('this.txt', 'w') as f:
    f.write(content)
    