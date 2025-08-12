with open('log.txt') as f:
   content = f.read()

if ("Python" in content):
       print(f"The word python is in the file.")
else:
       print(f"The word python is not in the file.")