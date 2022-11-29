# This is an input class. Do not edit.
from tkinter.messagebox import NO
from turtle import right, tracer


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# (h,d)
def binaryTreeDiameter(tree):
    if tree is None:
        return 0,0

    lHeight, lMaxDiameter = binaryTreeDiameter(tree.left)
    rHeight, rMaxDiameter = binaryTreeDiameter(tree.right)

    currentHeight = 1 + max(lHeight, rHeight)
    currentDiameter = lHeight + rHeight
    previousMaxDiameter = max(lMaxDiameter,rMaxDiameter)

    currentMaxDiameter = max(currentDiameter,previousMaxDiameter)

    return currentHeight,currentMaxDiameter




bt = BinaryTree(1)

bt.left = BinaryTree(3)
bt.right = BinaryTree(2)

bt.left.left = BinaryTree(7)
bt.left.right = BinaryTree(4)

bt.left.left.left = BinaryTree(8)
bt.left.right.right = BinaryTree(5)

bt.left.left.left.left = BinaryTree(9)
bt.left.right.right.right = BinaryTree(6)


print(binaryTreeDiameter(bt))