class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


head = BST(5)
head.left = BST(15)
head.left.left = BST(10)
head.left.right = BST(19)

head.right = BST(25)
head.right.right = BST(30)
head.right.left = BST(21)
head.right.left.right = BST(22)



def findKthLargestValueInBst(tree, k, array =[]):
 
    if tree is None:
        return -1

    if len(array) == k:
        return

    findKthLargestValueInBst(tree.right, k, array)

    if len(array) == k:
        return array[k-1]

    else:
        array.append(tree.value)
        findKthLargestValueInBst(tree.left, k, array)

    if len(array) == k:
        return array[k-1]
    else:
        return -1


print(findKthLargestValueInBst(head,3))


    

