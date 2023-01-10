# FIFO (First In First Out data structure.)

from collections import deque

class Queue():
    """
    Model a Queue class with enqueue, dequeue, peek methods.
    """
    def __init__(self):
        self.queue = deque()
        self.queue_size = 0
    
    def enqueue(self, element):
        # Insert an element to queue and increment queue size by 1
        self.queue.append(element)
        self.queue_size += 1
    
    def dequeue(self, element):
        # Pop the first element from the queue after checking queue size > 0
        # Decrement stack size by 1
        if self.queue_size > 0:
            self.queue_size -= 1
            return self.queue.popleft()
        else:
            return None
    
    def peek(self):
        # Check queue size > 0 then return the first value of queue
        if self.queue_size > 0:
            first_element = self.queue.popleft() # Pop out the first element and store it
            self.queue.appendleft(first_element) # Append the stored first element in front of queue
            return first_element
        else:
            return None
    
    def get_queue_size(self):
        return self.queue_size
    


# Test the wrapper class
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue) # 1
# print(q) # [2, 3, 4]
print(q.peek()) # 2
print("Queue size = ", q.get_queue_size())







        

