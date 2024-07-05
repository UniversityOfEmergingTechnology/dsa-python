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
    

def sumOfLongestBloddline(root):

    # helper function
    def dfs(node , current_sum , depth):

        if not node:
            return current_sum , depth
        
        # traverse left and right accumulating wealth and depth
        left_sum , left_depth = dfs(node.left , current_sum + node.value , depth + 1)
        right_sum , right_depth = dfs(node.right , current_sum + node.value , depth + 1)


        # if paths are of equal depth choose the wealthier , if not choose the longer
        if left_depth > right_depth :
            return left_sum , left_depth
        elif right_depth > left_depth : 
            return right_sum , right_depth
        else:
            return max(left_sum , right_sum) , left_depth


    # initiation
    max_sum , _ = dfs(root , 0 , 0)

    return max_sum

print("Start building the tree")
root = buildTree()


print(sumOfLongestBloddline(root))