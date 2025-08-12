class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        print(f"Adding {self.r} + {other.r}i and {self.i} + {other.i}j ")
        return Complex(self.r + other.r, self.i + other.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

    def __mul__(self, other):
        print(f"Multiplying {self.r * other.r} + {self.i * other.i}i and {self.r * other.i} + {self.i * other.r}j")
        return Complex(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __str__(self):
        return f"{self.r} + {self.i}i"
    


p = Complex(1, 2)
q = Complex(3, 4)
print(p + q)
print(p * q)