def minHeightBst(array):
    arrangedArray = arrangeItems(array,[])
    bst = None
    for item in arrangedArray:
        if bst is None:
            bst = BST(item)
            continue

        bst.insert(item)

    return bst
            
        

def arrangeItems(array, newArray = []):
 
    arrayLength = len(array)
    if arrayLength == 0:
        return

    if arrayLength == 1:
        newArray.append(array[0])
        return newArray

    if arrayLength%2 != 0:
        median = (arrayLength)//2
        newArray.append(array[median])
    else:
        median = (arrayLength)//2 -1
        newArray.append(array[median])


    arrangeItems(array[:median],newArray)
    arrangeItems(array[median + 1:],newArray)

    return newArray


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


    



print(minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22]))

print(minHeightBst([1]))