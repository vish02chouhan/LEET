# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    nodeFound = False

    if nodeFound:
        return 

    if  tree is None or tree.value == node:
        return tree


    treeNode = findSuccessor(tree.left,node)

    if treeNode is None and nodeFound == False:
        treeNode = findSuccessor(tree.right,node)

    if treeNode is None and nodeFound == False:
        return None

    if nodeFound == False and treeNode is treeNode.parent.left:
        nodeFound = True
        if treeNode.parent.right is None:
            return treeNode.parent.value
        return treeNode.parent.left.value

    if nodeFound == False and treeNode is treeNode.parent.right:
        nodeFound = True
        if treeNode.parent.parent is None:
            return treeNode.parent.value
        return treeNode.parent.parent.value
    



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
 
print(findSuccessor(bt,5))
    

