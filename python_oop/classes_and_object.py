# A Person class
class Person:

    def set_person_details(self, name, age):
        self.name = name
        self.age = age
        

    def display(self):
        print(f"I am a {self.name} from Person class.")

    def greet(self):
        if self.age < 30:
            print("How are you doing?")
        else:
            print("Nice day, isn't it?")
        self.display()
    

# Instances of Person class
p1 = Person()
p2 = Person()
# print(type(p1))

p1.set_person_details('Bob', 41)
p2.set_person_details('John', 23)

p1.greet(); p2.greet()

