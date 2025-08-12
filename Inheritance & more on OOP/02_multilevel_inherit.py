class Animals:
    pass

class Pets:
    pass

class Dogs(Animals, Pets):
    def display(self):
        print("This is a dog class")


a = Animals()
p = Pets()
d = Dogs()

d.display()