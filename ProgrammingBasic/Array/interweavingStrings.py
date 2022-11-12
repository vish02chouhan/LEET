class node:
    def __init__(self,value):
        self.value = value
        self.next = None

def interweavingStrings(one, two, three):
    dictOfThree = dictionaryOfString(three)

    lastItemIndex = -1
    result = True
    for idx,item in enumerate(one):

        if item in dictOfThree:
            itemValue = dictOfThree.pop(item)
            if not itemValue:
                break

            if type(itemValue) is int:
                if itemValue < lastItemIndex:
                    result = False
                    break
                else:
                    lastItemIndex = itemValue
            else:
                previousNode = None
                currentNode = itemValue
                while currentNode != None:
                    previousNode = currentNode
                    currentNode = currentNode.next
                
                nodeValue = currentNode.value
                previousNode.next = None
                
                if nodeValue < lastItemIndex:
                    result = False
                    break
                else:
                    lastItemIndex = itemValue
        else:
            break

    return result


def dictionaryOfString(three):
    keyValue = {}
    for idx,item in enumerate(three):
        if item in keyValue:
            itemValue = keyValue.pop(item)
            if type(itemValue) is int:
                newNode = node(idx)
                newNode.next = node(itemValue)
                keyValue[item] = newNode
            else:
                newNode = node(idx)
                newNode.next = itemValue
                keyValue[item] = newNode

        else:
            keyValue[item] = idx

    return keyValue