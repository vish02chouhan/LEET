# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    return traverseAndSum(root, 0 , [])



def traverseAndSum(root, sum, array ):
    if root is None:
        return array
        
    sum += root.value

    if root.left is None and root.right is None:
        array.append(sum)
        return array

    traverseAndSum(root.left, sum, array)
    traverseAndSum(root.right, sum, array)
    
    return array


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


bt1 = BinaryTree(1)
print(branchSums(bt))

print(branchSums(bt1))