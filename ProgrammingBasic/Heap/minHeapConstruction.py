# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
from email import header
from turtle import left, right

from numpy import iterable


class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap1(self, array):
        heapArray = []
        for item in array:
            if len(heapArray) == 0:
                heapArray.append(item)
                continue
            heapArray.append(item)
            for idx,iitem in enumerate(heapArray):
                leftChildItem = 2*idx+1
                rightChildItem = 2*idx+2
                if len(heapArray) > rightChildItem:
                    if heapArray[leftChildItem] < heapArray[rightChildItem] and heapArray[leftChildItem] < iitem:
                        (heapArray[leftChildItem],heapArray[idx]) = (heapArray[idx],heapArray[leftChildItem])
                    elif  heapArray[rightChildItem] < heapArray[leftChildItem] and heapArray[rightChildItem] < iitem:
                        (heapArray[rightChildItem],heapArray[idx]) = (heapArray[idx],heapArray[rightChildItem])
                    continue

                if len(heapArray) > leftChildItem:
                    if heapArray[leftChildItem] <  iitem:
                        (heapArray[leftChildItem],heapArray[idx]) = (heapArray[idx],heapArray[leftChildItem])
                        continue

        return heapArray       

    def buildHeap(self, array):


        return heapArray       

        

    def siftDown(self):
        # Write your code here.
        pass

    def siftUp(self):
        # Write your code here.
        pass

    def peek(self):
        # Write your code here.
        pass

    def remove(self):
        # Write your code here.
        pass

    def insert(self, value):
        # Write your code here.
        pass


minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])

print(minHeap.heap)