class Queue:

    def __init__(self):
        self.items = []
        print("consturcter")

    
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
q= Queue()
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)
q.enqueue(15)
print(q.peek())
print(q.size())
print(q.dequeue())
print(q.size())
print(q.items)