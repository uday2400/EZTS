class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None



def lo(root):
    if root is None:
        return
    
    q=[]
    
    q.append(root)
    # print(q)
    while len(q)>0:
        # n=q.pop(0)
        # print(n.value,end=" ")
        print(q[0].value,end=" ")
        n=q.pop(0)
        

        if n.left is not None:
            # print(n.left,end=" ")
            q.append(n.left)
        if n.right is not None:
            # print(n.right,end=" ")
            q.append(n.right)

        # print(q)








if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.left.right.left=node(9)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)

    root.left.right.right=node(10)
    root.right.left=node(6)
    root.right.right=node(7)
    root.right.right.right=node(11)
    lo(root)