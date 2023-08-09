# Class Employee
class Employee:

    def __init__(self, name, password, salary):
        self._name = name
        self._password = password
        self._salary = salary

    # Read only property : name
    @property
    def name(self):
        return self._name
    
    # Write only property : password
    @property
    def password(self):
        raise AttributeError('Password is not readable.')
    
    @password.setter
    def password(self, new_pass):
        self._password = new_pass
    
    # Read and Write property : Salary
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

# Instances
em = Employee('Jim', 'books1234', 10000)
print(em.name)
em.password = 'IlikeBooks123'
# print(em.password) # Error
print(em.salary)
em.salary = 12000
print(f"Reviewd Salary {em.salary}")






