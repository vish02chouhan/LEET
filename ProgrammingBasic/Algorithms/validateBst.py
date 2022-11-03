# This is an input class. Do not edit.
from array import array


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


head = BST(10)
head.left = BST(5)
head.left.right = BST(8)
head.right = BST(15)
head.right.right = BST(20)

def validateBst(tree, array = []):
    array = inOrderTraversal(tree,[])
    for index in range(0,len(array)-2):
        if array[index] > array[index+1]:
            return False
    

def inOrderTraversal(tree:BST, array=[]):
    if tree is None:
        return True

    inOrderTraversal(tree.left,array)
    array.append(tree.value)
    inOrderTraversal(tree.right,array)
  
    
    return array

def preOrderTraverse(tree, array):
    if tree is None:
          return
    array.append(tree.value)
    inOrderTraverse(tree.left, array)
    inOrderTraverse(tree.right, array)

    return array

validateBst(head)

    
