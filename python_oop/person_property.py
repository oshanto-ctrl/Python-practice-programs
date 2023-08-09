
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Person name {self.name} aged {self.age} years.")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 20 and value < 45:
            self._age = value
        else:
            raise ValueError("Age have to between 20 and 45")

# Instances
p = Person('Jim', 32)
print(p.age) # 32
p.age = 24
print(p.age) # 24
p.age = 46 # will raise an value error
print()

p1 = Person('Yen', 30)
p1.age = p1.age + 1
print(p1.age) # 31


