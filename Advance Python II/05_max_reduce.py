from functools import reduce
li = [43, 54, 67, 44]

max_val = reduce(lambda a, b : a if a> b else b, li)

print(max_val)

