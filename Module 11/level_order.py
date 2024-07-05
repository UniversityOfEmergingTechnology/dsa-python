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

def levelOrderTraversal(root):
    if not root :
        return


    queue = deque([root ,None])

    while queue:
        current_node = queue.popleft()
        if current_node == None :
            print()
            # we do not want this none marker when we are not having anything inside queue 
            if len(queue) > 0 :
                queue.append(None)
            continue

        print(current_node.value , end = ' ')

        if current_node.left :
            queue.append(current_node.left)
        
        if current_node.right :
            queue.append(current_node.right)


    

print("Start building the tree")
root = buildTree()
levelOrderTraversal(root)

