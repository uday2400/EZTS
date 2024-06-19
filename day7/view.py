class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None



def lo(root):
    if root is None:
        return
    
    # q=[]
    # a=[]
    # q.append(root)
    # # print(q)
    # while len(q)>0:
    #     # n=q.pop(0)
    #     # print(n.value,end=" ")
    #     # print(q[0].value,end=" ")
    #     n=q.pop(0)
        

    #     if n.left is not None:
    #         # print(n.left,end=" ")
    #         q.append(n.left)
    #     else:
    #         a.append(n.left)
        
    #     if n.right is not None:
    #         # print(n.right,end=" ")
    #         q.append(n.right)
    #     else:
    #         a.append(n.right)
            
    # print(a,end=" ")
        
    #         # print(n.value)

    # if (!root==None):






if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(5)
    root.left.left=node(3)
    root.left.right=node(4)
    root.left.right.left=node(9)
    # root.left.right.left.left=node(12)
    root.left.right.left.right=node(10)
    root.left.right.left.right.left=node(14)

    # root.left.right.right=node(10)
    # root.right.left=node(6)
    root.right.right=node(6)
    root.right.right.left=node(7)
    root.right.right.left.right=node(11)
    root.right.right.left.right.left=node(12)
    root.right.right.left.right.left.right=node(13)
    root.right.right.right=node(8)
    lo(root)