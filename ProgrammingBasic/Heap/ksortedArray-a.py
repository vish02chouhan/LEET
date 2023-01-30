#A min heap is a specific implementation of the heap data structure where the root node has 
# the minimum key among all the nodes in the heap. This means that the key of each node is less 
# than or equal to the key of its parent. In a min heap, the minimum element is always at the 
# root, making it easy to remove the minimum element efficiently.


#Insert
# To insert an element into a min heap, first the element is added to the bottom of the heap. 
# Then, the element is compared to its parent node. If the element is smaller than its parent, 
# it is swapped with its parent. This process is repeated until the element is in its correct 
# position and the heap property is restored.

#To delete an element from a min heap, the minimum element (the root node) is first removed. 
# The last element in the heap is then moved to the root position, and the heap is "bubbled down"
# to restore the heap property. This is done by comparing the key of the element with the keys 
# of its children and swapping it with the child that has the minimum key. 
# This process continues until the element is in its correct position and the heap property is 
# restored.

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0
    
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array
    
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
    
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
    
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove
    
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
    
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


def sortKSortedArray(array, k):
    minHeapWithKElements = MinHeap(array[: min(k + 1, len(array))])

    nextIndexToInsertElement = 0
    for idx in range(k + 1, len(array)):
        minElement = minHeapWithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1
        currentElement = array[idx]
        minHeapWithKElements.insert(currentElement)
    while not minHeapWithKElements.isEmpty():
        minElement = minHeapWithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1
    return array


print(sortKSortedArray([3, 2, 1, 5, 4, 7, 6, 5],3))
