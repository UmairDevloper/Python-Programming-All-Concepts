class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return (self.x * other.x - self.y * other.y,
                 self.x * other.y + self.y * other.x)

p = Complex(1, 2)
q = Complex(3, 4)
print(p + q)
print(p * q)