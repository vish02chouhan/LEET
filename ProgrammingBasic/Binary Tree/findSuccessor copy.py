# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
    (isSuccesor, parent) = findSuccessorHelper(tree, node)
    return parent

def findSuccessorHelper(tree, node):

    if tree is None:
        return (False, None)

    if tree.value == node.value:
        return (True, None)

    (isSuccesor, parent) = findSuccessorHelper(tree.left, node)

    if isSuccesor and parent is None:
        parent = tree.value

    if isSuccesor:
        return isSuccesor, parent

 
    if not isSuccesor:
        (isSuccesor, parent) = findSuccessorHelper(tree.right, node)
        if parent is None and isSuccesor:
                parent = tree.parent.value if tree.parent is not None else None
        
        if isSuccesor:
            return (True, parent)

        
        return (False, None)

    






    


bt = BinaryTree(1)

bt.left = BinaryTree(2)
bt.right = BinaryTree(3)
bt.left.parent = bt
bt.right.parent = bt

bt.left.left = BinaryTree(4)
bt.left.right = BinaryTree(5)
bt.left.left.parent = bt.left
bt.left.right.parent = bt.left

bt.left.left.left = BinaryTree(6)
bt.left.left.left.parent = bt.left.left
 
print(findSuccessor(bt,bt.left.right))