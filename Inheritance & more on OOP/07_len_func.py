class Complex:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)
    

ans = Complex([1, 2, 3])
print(len(ans))