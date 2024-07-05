class TreeNode :
    def __init__(self , key) -> None:
        self.val = key
        self.left = None
        self.right = None


class BinarySearchTree :
    def __init__(self) -> None:
        self.root = None
    

    def insert(self , key):
        # if its first node that's the root node
        if self.root is None:
            self.root = TreeNode(key)
        else :
            # this is my helper function which will allow me to insert node in bst
            self._insert(self.root , key)

    def _insert(self , node , key):

        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else :
                self._insert(node.left , key)
        else :
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right , key)
    
    def inorder_traversal(self , root):
        result = []

        if root :
            # in place addition of lists
            result += self.inorder_traversal(root.left)
            result.append(root.val)
            result += self.inorder_traversal(root.right)
 
        return result


bst = BinarySearchTree()
bst.insert(25)
bst.insert(12)
bst.insert(17)
bst.insert(33)
bst.insert(47)
bst.insert(35)
bst.insert(5)

result = bst.inorder_traversal(bst.root)

print(f"The inorder traversal of bst is {result}")
