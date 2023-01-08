class LinkedList:    
    def __init__(self, value):        
        self.value = value        
        self.next = None
        
        

# O(n) time | O(n) space - where n is the number of nodes in the Linked List
def linkedListPalindrome(head):    
    isPalindromeResults = isPalindrome(head, head)    
    return isPalindromeResults.outerNodesAreEqual
    
    

def isPalindrome(leftNode, rightNode):    
    if rightNode is None:        
        return LinkedListInfo(True, leftNode)    
    
    recursiveCallResults = isPalindrome(leftNode, rightNode.next)    
    leftNodeToCompare = recursiveCallResults.leftNodeToCompare    
    outerNodesAreEqual = recursiveCallResults.outerNodesAreEqual    
    recursiveIsEqual = outerNodesAreEqual and leftNodeToCompare.value == rightNode.value    
    nextLeftNodeToCompare = leftNodeToCompare.next    
    return LinkedListInfo(recursiveIsEqual, nextLeftNodeToCompare)
    
class LinkedListInfo:    
    def __init__(self, outerNodesAreEqual, leftNodeToCompare):        
        self.outerNodesAreEqual = outerNodesAreEqual        
        self.leftNodeToCompare = leftNodeToCompare



head = LinkedList(1) 

head.next = LinkedList(2)
head.next.next =LinkedList(3)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(2)
head.next.next.next.next.next = LinkedList(1)

linkedListPalindrome(head)