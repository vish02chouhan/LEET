# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self == None:
            return self

        newTreeNode = BST(value)

        if self.value == value:
            newTreeNode.right = self.right
            self.right = newTreeNode
            return

        curr = self
        while curr != None:
            if value < curr.value:
                if curr.left == None:
                    curr.left = newTreeNode
                    break
                curr = curr.left
            else:
                if curr.right == None:
                    curr.right = newTreeNode
                    break
                curr = curr.right
            
        return self

    def contains(self, value):

        curr = self

        while curr != None:
            if curr.value == value:
                return True

            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        return False

    def removeWhenBothLeftAndRightExists(self, parent):
        node = parent.right
        if node.left == None:
             parent.value = node.value
             parent.right = node.right
             node.right = None
             return True
        
        currentParent = parent
        while node.left != None:
            currentParent = node
            node = node.left

        if node.right != None:
            currentParent.left = node.right
            node.right = None
            parent.value = node.value

        currentParent.left = None
        parent.value = node.value
 

    def remove(self, value):
        curr = self
        parent = None
            
        
        while curr != None:
            if curr.value == value:
                if curr.left != None and curr.right != None:
                    self.removeWhenBothLeftAndRightExists(curr)
                    return True

                if curr.left == None and curr.right != None:
                    curr.value = curr.right.value
                    curr.right = curr.right.right
                    return True

                if curr.right == None and curr.left != None:
                    curr = curr.left.value
                    curr.left = curr.left.left
                    return True

                if curr.right == None and curr.left == None:
                    if parent == None:
                        parent.value = None

                    if value < parent.value:
                        parent.left = None
                    else:
                        parent.right = None
                
                break

            parent = curr
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
            
head =  BST(10)
head.insert(5)
head.insert(15)
head.remove(5)
head.remove(15)
head.remove(10)

print(head.contains(15))

a = 8
# head.insert(8)

# head.insert(24)

# head.insert(4)

# head.insert(12)

# head.insert(20)

# head.insert(28)

# head.insert(22)

# head.remove(20)

a =9