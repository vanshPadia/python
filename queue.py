class Queue:
    def __init__(self):
        self.queue_list = []

    def insert(self, value):
        self.queue_list.insert(0, value)

    def __str__(self):
        return f"Queue: {self.queue_list}"

# Create an instance of the Queue
q = Queue()

# Enqueue elements into the Queue
q.insert(12)
q.insert(23)

# Print the Queue
print(q)



class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")
    
    def size(self):
        return len(self.items)
