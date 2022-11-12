class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    (validBst, minValue) = validateBst1(tree, None)
    return validBst

def validateBst1(tree, isLeft):
     validBst = True
     if not tree and isLeft:
          return (True,float('-inf'))

     elif not tree and not isLeft:
          return (True, float('inf'))

     (validBst, minValue) = validateBst1(tree.left, True)
     if validBst:
          if tree.value <= minValue:
               return (False, tree.value)
          else:
              (validBst,maxValue) = validateBst1(tree.right, False)
              if validBst:
               if maxValue < tree.value:
                         return (False, tree.value)
               else:
                    if maxValue == float('inf'):
                         return (True,tree.value)
                    else:
                         return (True,maxValue)
     return (validBst, float('inf'))


bt = BinaryTree(10)

bt.left = BinaryTree(5)
bt.right = BinaryTree(15)

bt.left.left = BinaryTree(2)
bt.left.right = BinaryTree(5)

bt.right.right = BinaryTree(22)
bt.right.left = BinaryTree(13)

bt.left.left.left = BinaryTree(1)

bt.right.left.right = BinaryTree(16)


print(validateBst(bt))

# bt.right.right.right = BinaryTree(500)

# bt.right.right.right.left = BinaryTree(50)
# bt.right.right.right.left = BinaryTree(1500)

# bt.right.right.right.left.right = BinaryTree(200)

# bt.right.right.right.right = BinaryTree(10000)

# bt.right.right.right.right.left = BinaryTree(2200)
# bt.right.right.right.right.right = BinaryTree(9999)

