# linkedListOne = 6 -> 2 -> 3 -> 1 -> 4 -> 5                       
# linkedListTwo =      9->  8 -> 1 -> 4 -> 5

class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None




def mergingLinkedLists(linkedListOne, linkedListTwo):
    currentNodeOne = linkedListOne
    currentNodeTwo = linkedListTwo
    while currentNodeOne is not currentNodeTwo:
        if not currentNodeOne:
            currentNodeOne = linkedListTwo
        else:
            currentNodeOne = currentNodeOne.next

        if not currentNodeTwo:
            currentNodeTwo = linkedListOne
        else:
            currentNodeTwo = currentNodeTwo.next
    return currentNodeOne


common = LinkedList(1)
common.next = LinkedList(4)
common.next.next = LinkedList(5)

ll1 = LinkedList(6)
ll1.next = LinkedList(2)
ll1.next.next = LinkedList(3)
ll1.next.next.next = common

ll2 = LinkedList(9)
ll2.next = LinkedList(8)
ll2.next.next = common


mergingLinkedLists(ll1, ll2)