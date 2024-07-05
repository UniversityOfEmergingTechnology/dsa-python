class TreeNode:
    def __init__(self , val = 0 , left = None , right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def isCompleteTree(root):
    if not root:
        return True

    queue = [root]
    end = False

    while queue:
        current = queue.pop(0)

        if not current:
            end = True
        else:
            if end:
                return False
            
            queue.append(current.left)
            queue.append(current.right)

    return True

def isHeap(root):

    def isMaxHeap(node):
        if not node:
            return True

        if node.left and node.val < node.left.val:
            return False
        
        if node.right and node.val < node.right.val:
            return False
        
        return isMaxHeap(node.left) and isMaxHeap(node.right)

    def isMinHeap(node):

        if not node:
            return True
        
        if node.left and node.val > node.left.val:
            return False
        
        if node.right and node.val > node.right.val:
            return False

        return isMinHeap(node.left) and isMinHeap(node.right)

    # check if tree is a complete binary tree
    if not isCompleteTree(root):
        return False
    
    # check if tree satsfies either max heap or min heap
    return isMaxHeap(root) or isMinHeap(root)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(7)
# root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

print(isHeap(root))

    