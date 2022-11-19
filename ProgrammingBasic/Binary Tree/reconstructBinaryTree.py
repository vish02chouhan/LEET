class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None
        
    if len(preOrderTraversalValues) == 1:
        tree = BST(preOrderTraversalValues[0])
        return tree
    tree = BST(preOrderTraversalValues[0])
    
    indexOf = findIndex(preOrderTraversalValues, preOrderTraversalValues[0]) # index = 5
    if indexOf == -1:
        leftArray = preOrderTraversalValues[1:] # [4,2,1,5]
        rightArray = [] # [17, 19 , 18]
        return reconstructHelper(tree,leftArray, rightArray)
    else:        
        leftArray = preOrderTraversalValues[1:indexOf] # [4,2,1,5]
        rightArray = preOrderTraversalValues[indexOf:] # [17, 19 , 18]
        return reconstructHelper(tree,leftArray, rightArray)


def reconstructHelper(tree, leftArray, rightArray):
    if len(leftArray) == 0 and len(rightArray) == 0:
        return
    
    if len(leftArray) > 0:
        tree.left = BST(leftArray[0]) # 1.1 10 -> L -> 4 | 1.2 10 ->L->4-> L->2
        indexOf = findIndex(leftArray, leftArray[0]) # 1.1 index = 3| 1.2 index = - 1
        if indexOf == -1:
            ileftArray = leftArray[1:] #[1]
            irightArray = [] # []
            reconstructHelper(tree.left,ileftArray, irightArray)
        else:
            ileftArray = leftArray[1:indexOf] # 1.1 [2,1]
            irightArray = leftArray[indexOf:] # 1.1 [5]
            reconstructHelper(tree.left,ileftArray, irightArray)

    if len(rightArray) > 0: # 1.1 STACK [17,19,18] | 1.2 [5]
        tree.right = BST(rightArray[0])
        indexOf = findIndex(rightArray, rightArray[0])
        if indexOf == -1:
            ileftArray = rightArray[1:]
            irightArray = []
            reconstructHelper(tree.right,ileftArray, irightArray)
        else:
            ileftArray = rightArray[1:indexOf]
            irightArray = rightArray[indexOf:]
            reconstructHelper(tree.right, ileftArray, irightArray)
    
    return tree



def findIndex(array, element):
    for idx, item in enumerate(array):
        if idx == 0:
            continue
        if item >= element: 
            return idx
    return -1


tree = reconstructBst([10, 4, 2, 1, 5, 17, 19, 18])

abc =1