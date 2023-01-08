# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
  isFound, successor = helper(tree, node)
  if isFound:
      return successor

  return None


def helper(tree, node):

    if tree is None:
        return False

    isFound = True


    isFound, successor = helper(tree.left, node)

    if isFound and successor is not None:
        return isFound, successor
    elif isFound and successor is None:
        return isFound, tree

    isFound, successor = helper(tree.right, node)
    if isFound and successor is not None:
        return isFound, successor
    elif isFound and successor is None:
        return isFound, None

    return False, None




    


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