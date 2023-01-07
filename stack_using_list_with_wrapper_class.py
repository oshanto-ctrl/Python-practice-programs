class Stack():
    """Model a stack class that use push, pop, peek methods."""

    def __init__(self):
        self.stack = list()
    
    def push(self, element):
        self.stack.append(element) # Push element into stack
    
    def pop(self):
        # Check size of the stack
        # If size of stack > 0 then pop
        # Else return None
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    
    def peek(self):
        # Check size of the stack
        # If size of stack > 0 then check the top element
        # Else return None
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    
    def __str__(self):
        # Print out the stack with string representation
        return str(self.stack)

# Testing the wrapper class

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack) # O/P = [1, 2, 3, 4]
print(my_stack.pop()) # O/P = 4
print(my_stack.peek()) # O/p = 3
print(my_stack.pop()) # O/P = 3
print(my_stack) # [1, 2]











