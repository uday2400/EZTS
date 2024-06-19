class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def left_view(root):
    if root is None:
        return
    
    # Queue for level order traversal
    queue = [root]
    
    while queue:
        # Number of nodes at the current level
        level_length = len(queue)
        
        # Traverse all nodes at the current level
        for i in range(level_length):
            node = queue.pop(0)
            
            # Print the first node of each level
            if i == 0:
                print(node.value, end=" ")
            
            # Enqueue left child
            if node.left:
                queue.append(node.left)
            
            # Enqueue right child
            if node.right:
                queue.append(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(9)
    root.left.right.left.left = Node(12)
    root.left.right.left.right = Node(13)
    root.left.right.right = Node(10)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.right = Node(11)
    
    left_view(root)
