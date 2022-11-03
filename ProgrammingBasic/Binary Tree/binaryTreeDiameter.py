# This is an input class. Do not edit.
from tkinter.messagebox import NO
from turtle import right


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):

    parent = tree
    untraversedNodes = [parent]
    max = 0
    while untraversedNodes:
        currentNode = untraversedNodes.pop(0)
        if currentNode.left is None and currentNode.right is None:
            continue

        if currentNode.left is not None and currentNode.right is not None:
            diameter = calculateDiameter(currentNode)
            if diameter > max:
                max = diameter
            untraversedNodes.append(currentNode.left)
            untraversedNodes.append(currentNode.right)
            continue

        if currentNode.left is not None:
            untraversedNodes.append(currentNode.left)
            continue

        if currentNode.right is not None:
            untraversedNodes.append(currentNode.right)
            continue




    # Write your code here.
    return max

def calculateDiameter(tree):


    parent = tree
    untraversedNodes = [parent.left, parent.right]
    diameter = 2
    while untraversedNodes:
        currentNode = untraversedNodes.pop(0)

        if currentNode.left is not None and currentNode.right is not None:
            continue

        if currentNode.left is None and currentNode.right is None:
            continue

        if currentNode.left is not None:
            diameter += 1
            untraversedNodes.append(currentNode.left)

        if currentNode.right is not None:
            diameter += 1
            untraversedNodes.append(currentNode.right)
    
    return diameter
    


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