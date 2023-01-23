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
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParent = (len(array) - 1)//2

        for parent in reversed(range(firstParent + 1)):
            self.siftDown(parent, array)

        

    def siftDown(self, parent, heap):

        firstChild = parent * 2 + 1
        while firstChild < len(heap):
            secondChild  = firstChild + 1 if firstChild + 1 < len(heap) else -1

            swapContainder = -1

            if secondChild != -1 and heap[secondChild] < heap[firstChild]:
                swapContainder = secondChild
            else:
                swapContainder = firstChild

            if heap[swapContainder] < heap[parent]:
                heap[swapContainder], heap[parent] = heap[parent], heap[swapContainder]
                parent = swapContainder
                firstChild = parent * 2 + 1
            else:
                break

        
        pass

    def siftUp(self):
        firstChild = -1
        secondChild = -1
        if len(self.heap) %2 == 0:
            firstChild = len(self.heap)- 2
            secondChild = len(self.heap)- 1
        else:

            parent = (child -1)// 2


        pass

    def peek(self):
        # Write your code here.
        pass

    def remove(self):
        # Write your code here.
        pass

    def insert(self, value):
        self.heap.append(value)
        self.shiftUp()
        pass


minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])

print(minHeap.heap)
