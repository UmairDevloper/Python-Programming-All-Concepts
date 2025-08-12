class Two_d_Vector:
    # It is the constructor of the Python It perform its function same like C++ constructor 
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"the vector has values as {self.i}i ans {self.j}j")

class Three_d_Vector(Two_d_Vector):
    # initializing the value of i, j and k it means that this class need 3 variables i, j and k 
    def __init__(self, i, j, k):
        # calling the parent class constructor
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"the vector has values as {self.i}i ans {self.j}j ans {self.k}k")


v1 = Two_d_Vector(1, 2)
v1.show()

v2 = Three_d_Vector(1, 2, 3)
v2.show()
