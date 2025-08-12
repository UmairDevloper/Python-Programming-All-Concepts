class Programmer:
    company = "Microsoft"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

p = Programmer("John", 25, 100000)
print(p.company, p.name, p.age, p.salary)
r = Programmer("Maddi", 25, 100000)
print(r.company, r.name, r.age, r.salary)
