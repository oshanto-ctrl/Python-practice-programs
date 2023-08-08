class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("I am ", self.name)
    
    def greet(self):
        if self.age > 30:
            print("How are you doing?")
        else:
            print("How do you do?")
        self.display()

# Instances
p = Person("Priya", 30)
p.greet()

p2 = Person("John", 41)
p2.greet()