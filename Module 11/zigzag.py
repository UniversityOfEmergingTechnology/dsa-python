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
    

def zizagLevelOrder(root):
    if not root :
        return []
    

    results = []

    current_level = deque([root])
    left_to_right = True

    while current_level :
        level_size = len(current_level)
        level_values = []

        for _ in range(level_size):
            node = current_level.popleft()
            # add the node value to level_values list
            level_values.append(node.value)
        
            # append child nodes in the queue
            if node.left :
                current_level.append(node.left)
            
            if node.right :
                current_level.append(node.right)

        # if traversal direct is right to left reverse it
        if not left_to_right :
            level_values.reverse()
        
        results.append(level_values)
        left_to_right = not left_to_right
    
    return results



root = buildTree()

print(zizagLevelOrder(root))



