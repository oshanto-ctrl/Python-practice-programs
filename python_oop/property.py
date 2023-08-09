# Learning about property

class Product:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)
    
    # Act as get value method self._x
    @property
    def get_x(self):
        return self._x

    # Act as set value method to self._x
    @get_x.setter
    def set_x(self, val):
        self._x = val

    # Act as get value method self._y
    @property
    def get_y(self):
        return self._y

    # Act as set value to self._y
    @get_y.setter
    def set_y(self, val):
        self._y = val


# Instances
p = Product(12, 24)

# for x

print(p.get_x) # 12
# print(dir(Product))
# Setting a new value to p.set_x
# p.set_x = 200 # got an attribute error.

# With @get_x.setter now we can add new value to self._x
p.set_x = 200
print(p.get_x) # 200

# for y
print('Y ', p.get_y) # 24

p.set_y = 300

print('Y ', p.get_y) # 300
