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
    
def verticalOrder(root):
    if not root :
        return []

    column_table = defaultdict(list)
    queue = deque([(root , 0)]) # (node , column_index)

    while queue:
        node , column = queue.popleft()

        if node :
            column_table[column].append(node.value)
            queue.append((node.left , column - 1))
            queue.append((node.right , column + 1))
        
    
    # extracting columns sorted by their horizontal distance
    return [column_table[x] for x in sorted(column_table)]

root = buildTree()

print(verticalOrder(root))