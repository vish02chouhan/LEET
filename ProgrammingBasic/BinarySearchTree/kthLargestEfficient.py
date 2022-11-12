class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class treeInfo:
    def __init__(self, index, value):
        self.index = index
        self.value = value


def findKthLargestValueInBst(tree, k):
    treeInfo = treeInfo(-1,-1)
    return findKthLargestValueInBstHelper(tree, k, treeInfo)

def findKthLargestValueInBstHelper(tree, k, index, treeInfo):
    if tree is None:
        return

    findKthLargestValueInBstHelper(tree.right , treeInfo)
    treeInfo.index += 1 
    if treeInfo.index == k:
        return treeInfo
    else:
        findKthLargestValueInBstHelper(tree.left , treeInfo)

    
    return



head = BST(15)
head.left = BST(5)
head.right = BST(20)

head.left.left = BST(2)
head.left.right = BST(5)

head.right.left = BST(17)
head.right.right = BST(22)

head.left.left.left = BST(1)
head.left.left.right = BST(3)


    

