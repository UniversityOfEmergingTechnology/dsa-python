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
    

def bottomView(root):
    if not root :
        return []
    
    # dictionary to hold final node at each horizontal distance
    hd_node_map = {}
    queue = deque([(root , 0)]) # node , distance

    while queue:
        node , hd = queue.popleft()

        # update the dictionary with latest node for each horizontal distance
        hd_node_map[hd] = node.value

        # enqueue the left and right children with updated horizontal distance
        if node.left :
            queue.append((node.left , hd - 1))
        
        if node.right:
            queue.append((node.right , hd + 1))
    
    return [hd_node_map[hd] for hd in sorted(hd_node_map)]

print("Start building the tree")
root = buildTree()


print(bottomView(root))
