class BST:
    def __init__(self, value, left=None, right=None):
            self.value = value        
            self.left = left        
            self.right = right

class TreeInfo:    
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
                self.numberOfNodesVisited = numberOfNodesVisited
                self.latestVisitedNodeValue = latestVisitedNodeValue# O(h + k) time | O(h) space - where h is the height of the tree and k is the input parameter
                
def findKthLargestValueInBst(tree, k):
       treeInfo = TreeInfo(0, -1)
       reverseInOrderTraverse(tree, k, treeInfo)    
       return treeInfo.latestVisitedNodeValue
       
def reverseInOrderTraverse(node, k, treeInfo):    
       if node is None or treeInfo.numberOfNodesVisited >= k:        
        return  

       reverseInOrderTraverse(node.right, k, treeInfo)    
       if treeInfo.numberOfNodesVisited < k:        
            treeInfo.numberOfNodesVisited += 1        
            treeInfo.latestVisitedNodeValue = node.value        
            reverseInOrderTraverse(node.left, k, treeInfo)

head = BST(15)
head.left = BST(5)
head.right = BST(20)

head.left.left = BST(2)
head.left.right = BST(5)

head.right.left = BST(17)
head.right.right = BST(22)

head.left.left.left = BST(1)
head.left.left.right = BST(3)

findKthLargestValueInBst(head,3)