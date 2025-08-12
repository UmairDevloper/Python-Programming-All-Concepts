class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment
    
    def beforeIncrement(self):
        print(f"Your salary before increment is {self.salary}")

    @property
    def afterIncrement(self):
        self.salary = self.salary + self.increment
        print(f"Your salary after increment is {self.salary}")

    @afterIncrement.setter
    def afterIncrement(self, value):
        self.increment = value
    
   

p = Employee(5000, 500)
p.beforeIncrement()
p.after_inc = 1000
p.afterIncrement

