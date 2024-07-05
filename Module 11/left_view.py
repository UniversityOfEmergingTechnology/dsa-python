from collections import deque

class TreeNode:
    def __init__(self , value = 0) -> None:
        self.value = value
        self.left = None
        self.right = None
    
def buildTree():
    inputValue = int(input("Enter node value (-1 for no node) : "))

    # base case
    if inputValue == -1 :
        return None
        
    # create a node
    node = TreeNode(inputValue)

    # recursively ask user for left and right child
    print(f"Enter left child of {inputValue}")
    node.left = buildTree()

    print(f"Enter right child of {inputValue}")
    node.right = buildTree()


    return node
    

def leftView(root):
    if not root :
        return root

    result = []

    queue = deque([root])

    while queue:
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()

            # capture first node of level
            if i == 0 :
                result.append(node.value)

            # enqueue child nodes
            if node.left :
                queue.append(node.left)
            
            if node.right :
                queue.append(node.right)
    
    return result


print("Start building the tree")
root = buildTree()

print(leftView(root))
