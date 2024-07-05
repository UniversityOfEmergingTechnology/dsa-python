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

def isSumTree(node):
    # base case
    if node is None or (node.left is None and node.right is None) :
        return True , node.value if node else 0
    
    # recursive step

    left_is_sum , left_sum = isSumTree(node.left)
    right_is_sum , right_sum = isSumTree(node.right)

    node_is_sum = left_is_sum and right_is_sum and (node.value == left_sum + right_sum)

    return node_is_sum ,  left_sum + right_sum

    

print("Start building the tree")
root = buildTree()

answer, sum = isSumTree(root)

print("the sum is ",sum)

print("The answer is ", answer)