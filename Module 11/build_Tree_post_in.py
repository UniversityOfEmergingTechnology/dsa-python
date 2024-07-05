from collections import deque

class TreeNode:
    def __init__(self , value = 0) -> None:
        self.value = value
        self.left = None
        self.right = None

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


def buildTree(inorder , postorder):

    if not inorder or not postorder :
        return None

    # the last element in postorder is root
    root_val = postorder[-1]
    root = TreeNode(root_val)

    # split inorder list into left and right subtrees

    mid = inorder.index(root_val)

    # recursively build left and right subtree
    root.left = buildTree(inorder[:mid] , postorder[:mid])
    root.right = buildTree(inorder[mid + 1:] , postorder[mid:-1])

    return root

postorder = [4,5,2,6,7,3,1]
inorder = [4,2,5,1,6,3,7]

root =  buildTree(inorder , postorder)

levelOrderTraversal(root)
