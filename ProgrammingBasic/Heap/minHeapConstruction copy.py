# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41] - 14 length

    def buildHeap(self, array):
        arrayLength = len(array)
        lastIndex = arrayLength - 1
        parent = (lastIndex - 1)//2
        while parent >= 0:

            left = 2*parent + 1
            right = 2*parent + 2
           

            if right >= arrayLength:
                if array[left] > array[parent]:
                    (array[parent],array[left]) = (array[left],array[parent])
            
            else:
                if array[left] < (array[right] and array[parent]):
                    (array[parent],array[left]) = (array[left],array[parent])
                elif array[right] < (array[left] and array[parent]):
                     (array[parent],array[right]) = (array[right],array[parent])

            parent = parent - 1

        return array

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