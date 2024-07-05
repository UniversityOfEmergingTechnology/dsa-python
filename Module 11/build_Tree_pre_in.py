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


def buildTree(preorder , inorder) :

    if not preorder or not inorder:
        return None


    # root is the first element in preorder list
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    # recursively construct left and right subtree

    root.left = buildTree(preorder[1 : mid + 1] , inorder[:mid])
    root.right = buildTree(preorder[mid + 1 :] , inorder[mid + 1 :])


    return root


preorder = [3, 9 , 20, 15,7]
inorder = [9,3,15,20,7]

root = buildTree(preorder , inorder)

levelOrderTraversal(root)
