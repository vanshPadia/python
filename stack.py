class stack:
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item =[item]+ self.item
        return self.item
    def pop(self):
        self.item.pop(0)
        return self.item
s =stack()
print(s.pop())
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.item)

# print(s.pop())
# s.push(10)
# print(s.item)
# print(s.pop())
# print(s.pop())

