##QUEUE

class Queue:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop(0)
    def size(self):
        print(len(self.items))
a=Queue()
a.push(10)
a.push(20)
a.push(30)
print(a.items)
a.pop()
print(a.items)
