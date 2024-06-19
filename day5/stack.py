class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        print(len(self.items))

        
        
        
        
        
        
s=Stack()

s.push(10)
s.push(20)

s.push(30)

print(s.items)
s.pop()
print(s.items)
s.size()