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
        
    def buildHeap(self, array):     
        first_parent = (len(array) - 1) // 2        
        for parent in reversed(range(first_parent + 1)):
            self.siftDown(parent, len(array)-1, array)        
        return array    
            
    def siftDown(self, cidx, endidx, heap):        
        child_one_idx = cidx * 2 + 1              
        while child_one_idx <= endidx:            
            child_two_idx = cidx * 2 + 2 if cidx * 2 + 2 <= endidx else -1            
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:                   
                potential_swap_idx = child_two_idx            
            else:                              
                potential_swap_idx = child_one_idx                      
            
            if heap[potential_swap_idx] < heap[cidx]:                              
                    self.swap(cidx, potential_swap_idx, heap)                
                    cidx = potential_swap_idx
                    child_one_idx = cidx * 2 +1
            else:
                    break


    def siftUp(self,idx,heap):
        parent_idx = (idx-1)//2
        while idx > 0 and heap[idx] < heap[parent_idx]:
            self.swap(idx,parent_idx, heap)
            idx = parent_idx
            parent_idx = (idx-1)//2

    def remove(self):               
        self.swap(0, len(self.heap)-1, self.heap)              
        min_value = self.heap.pop()              
        self.siftDown(0, len(self.heap)-1, self.heap)          
        return min_value    
    
    def insert(self, value):         
        self.heap.append(value)               
        self.siftUp(len(self.heap)-1, self.heap)  

    def peek(self):
      return self.heap[0]
    
    def swap(self, idx1, idx2, heap):             
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]




minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])

debug = True