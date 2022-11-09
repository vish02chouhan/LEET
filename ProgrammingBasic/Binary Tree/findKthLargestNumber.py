class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k, index = 0):
    if tree is None:
        return 0

    current = findKthLargestValueInBst(tree.left,k, index)
    index = index + 1 +  current
    if index < k:
      
        index = index + findKthLargestValueInBst(tree.right,k, index)

    return index


def findKthLargestValueInBst1(tree, k):
    array=[]
    print(inOrderTraversal(tree,array))

    return array


def inOrderTraversal(tree, array=[]):
    if tree is None:
        return

    inOrderTraversal(tree.left,array)
    array.append(tree.value)
    inOrderTraversal(tree.right,array)

    return array

head = BST(15)
head.left = BST(5)
head.right = BST(20)

head.left.left = BST(2)
head.left.right = BST(5)

head.right.left = BST(17)
head.right.right = BST(22)

head.left.left.left = BST(1)
head.left.left.right = BST(3)

findKthLargestValueInBst(head,3)

