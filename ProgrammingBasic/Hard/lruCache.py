# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.


class Node:
     def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.head = None
        self.currentSize = 0

    def insertKeyValuePair(self, key, value):
            
            if self.head == None:
                self.head = Node(key, value)
                self.currentSize +=1
                return


            node = self.getKeyIfExists(key)

            if node is None:
                if self.currentSize == self.maxSize:
                    if self.evictLastOne() is not True:
                         return None
                node = Node(key,value)
                self.currentSize += 1
            else:
                node.value = value

            node.next = self.head
            self.head = node

    def evictLastOne(self):
        if self.head is None:
            return False

        if self.currentSize == 1:
            self.head = None


        currentNode = self.head
        previousNode = None

        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next

        previousNode.next = None
        self.currentSize -=1
        return True


    def getKeyIfExists(self,key):
        if self.head is None:
            return None

        if self.head.key == key:
            return self.head

        currentNode = self.head
        previousNode = None

        while currentNode is not None:
            if currentNode.key == key:
                previousNode.next = currentNode.next
                return currentNode

            previousNode = currentNode
            currentNode = currentNode.next

        return None

    def getValueFromKey(self, key):
        node = self.getKeyIfExists(key)

        if node is not None:
            node.next = self.head
            self.head = node
            return self.head.value

        
        return None

    def getMostRecentKey(self):
        return self.head.key


cache = LRUCache(3)
cache.insertKeyValuePair("b",2)
cache.insertKeyValuePair("a",1)
cache.insertKeyValuePair("c",3)
valGet = cache.getMostRecentKey()

valGet1 = cache.getValueFromKey('a')
valGet2 = cache.getMostRecentKey()
cache.insertKeyValuePair("d",4)
valGet4 = cache.getValueFromKey('b')
cache.insertKeyValuePair("a",5)
valGet5 = cache.getValueFromKey('a')
x = 4