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
    def __init__(self):
        self.heap =[]

    
    def push(self,value):
        if len(self.heap) == 0:
            self.heap.append(value)
        else:
            self.heap.append(value)
            self.bubbleUp()

    def pop(self):
        if len(self.heap) == 1:
            self.heap.pop(0)
        else:
            self.heap[0] = self.heap[len(self.heap) - 1]
            self.heap.pop()
            self.bubbleDown()


    def bubbleUp(self):
        index = len(self.heap)-1

        #condition to handel
        # 1) for example parent is 10
        # 2) New Element is 8
        # 3)
        while index > 0:
            parent = (index-1)//2
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                return 
    
    def bubbleDown(self):
        index = 0


        while index < len(self.heap):
            leftChild = index*2 + 1
            rightChild = index*2 + 2
            if rightChild < len(self.heap):
                if self.heap[rightChild] < min(self.heap[leftChild],self.heap[index]):
                    self.heap[rightChild], self.heap[index] = self.heap[index],self.heap[rightChild]
                    index = rightChild
                elif self.heap[leftChild] < self.heap[index]:
                    self.heap[leftChild], self.heap[index] = self.heap[index],self.heap[leftChild]
                    index = leftChild
                else:
                    break



minHeap = MinHeap()

minHeap.push(17)
minHeap.push(27)
minHeap.push(7)
minHeap.push(32)
minHeap.push(26)
minHeap.push(29)
minHeap.push(23)
minHeap.push(24)
minHeap.push(31)
minHeap.push(32)
minHeap.push(34)

print(minHeap.heap)

