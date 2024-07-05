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

def maxDepth(root):
    # base case
    if not root:
        return 0
    
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)

    return max(left_height , right_height) + 1

print("Start building the tree")
root = buildTree()
print("Depth of the tree is " ,  maxDepth(root))

