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
    

def isLeaf(node) :
    return node.left is None and node.right is None

def addLeaves(res , root) :
    if isLeaf(root):
        res.append(root.value)
    if root.left:
        addLeaves(res,root.left)
    if root.right :
        addLeaves(res , root.right)

def boundaryTraversal(root):

    if not root :
        return []

    res = []

    if not isLeaf(root) :
        res.append(root.value)

    # left boundary
    t = root.left

    while t:
        if not isLeaf(t):
            res.append(t.value)
        t = t.left if t.left else t.right
    

    # add leaves
    addLeaves(res , root)


    # right boundary

    stack = []

    t = root.right

    while t :
        if not isLeaf(t):
            stack.append(t.value)
        t = t.right if t.right else t.left
    
    while stack :
        res.append(stack.pop())
    
    return res
        

root = buildTree()

print(boundaryTraversal(root))