class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
    
head=tail=Node(10)
# tail=tail.next

tail.next=Node(20)
tail=tail.next
tail.next=Node(30)
tail=tail.next
tail.next=Node(40)
tail=tail.next
print(head)
print(head.value)
# head=100

def print_list(head):
    curr=head
    while curr:
        print(curr.value,end="->")
        curr=curr.next
    print("None")

print_list(head)

