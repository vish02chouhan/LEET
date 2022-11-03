def invertBinaryTree(tree):
    if tree is None:
        return

    untraversedNodes = []
    untraversedNodes.append(tree)
    untraversedNodes.append(tree.left)
    untraversedNodes.append(tree.right)
    while untraversedNodes:
        currentNode = untraversedNodes.pop(0)
        currentNodeLeft = untraversedNodes.pop(0)
        currentNodeRight = untraversedNodes.pop(0)

        if currentNodeLeft is None and currentNodeRight is None:
            continue

        if currentNodeLeft is not None and  currentNodeRight is not None:
            temp = currentNode.left
            currentNode.left = currentNode.right
            currentNode.right = temp

            untraversedNodes.append(currentNodeLeft) 
            untraversedNodes.append(currentNodeLeft.left) 
            untraversedNodes.append(currentNodeLeft.right) 
            untraversedNodes.append(currentNodeRight) 
            untraversedNodes.append(currentNodeRight.left) 
            untraversedNodes.append(currentNodeRight.right) 

        elif currentNodeLeft is None:
            untraversedNodes.append(currentNodeRight) 
            untraversedNodes.append(currentNodeRight.left) 
            untraversedNodes.append(currentNodeRight.right) 

        elif currentNodeRight is None:
            untraversedNodes.append(currentNodeLeft) 
            untraversedNodes.append(currentNodeLeft.left) 
            untraversedNodes.append(currentNodeLeft.right) 

        
        
        



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

bt = BinaryTree(1)

bt.left = BinaryTree(2)
bt.right = BinaryTree(3)

bt.left.left = BinaryTree(4)
bt.left.right = BinaryTree(5)

# bt.right.left = BinaryTree(6)
# bt.right.right = BinaryTree(7)

# bt.left.left.left = BinaryTree(8)
# bt.left.left.right = BinaryTree(9)

print(invertBinaryTree(bt))