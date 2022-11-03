class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


head = BST(16)
head.left = BST(8)
head.left.right = BST(12)
head.left.left = BST(4)
head.right = BST(24)
head.right.right = BST(28)
head.right.left = BST(20)



def inOrderTraverse(tree, depth = 0):

    if tree is not None and tree.right is None:
        depth +=1
        print(str(depth) + 'Highest')
    if tree is None:
          return depth
    depth = inOrderTraverse(tree.right,depth)
    print(tree.value)
    depth = inOrderTraverse(tree.left, depth)
   
    

inOrderTraverse(head)