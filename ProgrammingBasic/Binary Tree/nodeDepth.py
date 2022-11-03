def nodeDepths(root):
    
    levelNodes =[]
    untraversedNodes = [root]

    while untraversedNodes:
        tempArray = []
        levelNodesTemp = []
        while len(untraversedNodes)> 0:
            currentNode = untraversedNodes.pop(0)
            levelNodesTemp.append(currentNode)
            if currentNode.left is not None:
                tempArray.append(currentNode.left)
            
            if currentNode.right is not None:
                tempArray.append(currentNode.right)
        
        for item in tempArray:
            untraversedNodes.append(item)

        levelNodes.append(levelNodesTemp)

    sum = 0
    for idx,item in enumerate(levelNodes):
        
        sum += idx * len(item)

    return sum



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

bt.right.left = BinaryTree(6)
bt.right.right = BinaryTree(7)

bt.left.left.left = BinaryTree(8)
bt.left.left.right = BinaryTree(9)

bt.left.right.left = BinaryTree(10)

print(nodeDepths(bt))