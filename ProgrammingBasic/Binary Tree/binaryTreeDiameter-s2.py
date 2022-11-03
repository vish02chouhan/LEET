# This is an input class. Do not edit.
from tkinter.messagebox import NO
from turtle import right, tracer


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    if tree is None:
         return 0

    max = 0

    for item in getBfsArray(tree):
      diameter =  getDiameter(item.left) + getDiameter(item.right)
      if diameter > max:
        max = diameter
    
    return max


def getBfsArray(tree):
    stack = []
    bfsArray = []
    stack.append(tree)
    while stack:
        untraversedNode = stack.pop(0)
        if untraversedNode:
            bfsArray.append(untraversedNode)
            stack.append(untraversedNode.left)
            stack.append(untraversedNode.right)

    return bfsArray
        
 
def getDiameter(tree):

    if tree is None:
        return 0

    diameterLeft = 1+ getDiameter(tree.left) 
    diameterRight = 1+ getDiameter(tree.right)
    return max(diameterLeft, diameterRight) 



bt = BinaryTree(1)

bt.left = BinaryTree(3)
bt.right = BinaryTree(2)

bt.right.left = BinaryTree(7)
bt.right.right = BinaryTree(4)

bt.right.left.left = BinaryTree(8)
bt.right.right.right = BinaryTree(5)

bt.right.left.left.left = BinaryTree(9)
bt.right.right.right.right = BinaryTree(6)


print(binaryTreeDiameter(bt))