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

def preorderTraversal(root):
    if root :
        # nlr
        print(root.value , end = ' ')
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def inorderTraversal(root):
    if root :
        # lnr
        inorderTraversal(root.left)
        print(root.value , end = ' ')
        inorderTraversal(root.right)

def postorderTraversal(root):
    if root :
        # lrn
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.value , end = ' ')


print("Start building the tree")
root = buildTree()
print("Preorder traversal")
preorderTraversal(root)
print()
print()
print("Inorder traversal")
inorderTraversal(root)
print()
print()
print("Postorder traversal")
postorderTraversal(root)

# 1 2 4 -1 -1 5 -1 -1 3 6 -1 -1 7 -1 -1
