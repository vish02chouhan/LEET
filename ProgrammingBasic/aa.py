def mergingLinkedLists(linkedListOne, linkedListTwo):
    llOneLength = 0
    llTwoLength = 0
    currentNode = linkedListOne
        
    while currentNode is not None:
        llOneLength += 1
        currentNode = currentNode.next
        currentNode = linkedListTwo
    
    while currentNode is not None:
            llTwoLength += 1
            currentNode = currentNode.next
			
    if llOneLength > llTwoLength:
        while llOneLength != llTwoLength:
            linkedListOne = linkedListOne.next
            llOneLength -= 1
    else:
        while llOneLength != llTwoLength:
            linkedListTwo = linkedListTwo.next
            llTwoLength -= 1

    while linkedListOne is not None:
        if linkedListOne == linkedListTwo:
            return linkedListOne
        else:
            linkedListOne = linkedListOne.next
            linkedListTwo = linkedListTwo.next

    return None
