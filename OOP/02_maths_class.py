class Operations:

    @staticmethod
    def square(a):
        return a*a
    
    @staticmethod
    def cube(a):
        return a*a*a
    
    @staticmethod
    def square_root(a):
        return a**0.5
    

ans = Operations()
print(ans.square(4))
print(ans.cube(4))
print(ans.square_root(4))