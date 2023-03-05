class Shape():
    def __init__(self, dimension1, dimension2):
        self.dimension1 = dimension1
        self.dimension2 = dimension2
    
    def area(self):
        print("I am area() method in Shape Class.")


class Triangle(Shape):

    def area(self):
        area = 0.5 * self.dimension1 * self.dimension2
        print("Triangular Area = ", area)


class Rectangle(Shape):

    def area(self):
        area = self.dimension1 * self.dimension2
        print("Rectangular Area = ", area)

# instances of Triangle

t = Triangle(20, 30)
print(t.area())

# instances of Rectangel
r = Rectangle(20, 30)
print(r.area())

