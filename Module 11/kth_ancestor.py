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
    


def findKthAncestor(root , target_value , k) :
    # helper function to navigate the tree and record the path
    def dfs(node , target_value , path):
        if not node :
            return False

        path.append(node)

        # target found or continue searching
        if node.value == target_value or dfs(node.left , target_value, path) or dfs(node.right , target_value, path)  :
            return True

        # wrong path backtrack
        path.pop()        
        return False

    path = []
    if dfs(root , target_value , path) and len(path) >= k + 1 :
        return path[-(k + 1)].value
    
    return "Kth ancestor does not exist"

print("Start building the tree")
root = buildTree()

print(findKthAncestor(root , 5 , 2))





