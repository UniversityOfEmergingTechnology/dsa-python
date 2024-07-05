from collections import deque , defaultdict

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

def diagonalTraversal(root) :
    if not root :
        return []

    diagonal_map = defaultdict(list)

    queue = deque([(root , 0)]) # node , diagonal


    while queue:

        node , d = queue.popleft()

        diagonal_map[d].append(node.value)

        # right child remains on the same diagonal
        if node.right :
            queue.append((node.right , d))

        # left child moves to the next diagonal
        if node.left:
            queue.append((node.left , d + 1))
        

    # flatten the dictionary to get desired diagonal order
    return [val for key in sorted(diagonal_map) for val in diagonal_map[key] ]

print("Start building the tree")
root = buildTree()

print(diagonalTraversal(root))

