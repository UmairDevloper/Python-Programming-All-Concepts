
def divisible(n):
    if n % 5 == 0:
        return True
    return False
    
li = [34, 54, 6, 4, 3, 54,6767677, 25, 55, 345]

val = list(filter(divisible, li))

print(val)