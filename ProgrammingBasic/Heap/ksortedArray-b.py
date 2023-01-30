# {
#   "array": [3, 2, 1, 5, 4, 7, 6, 5],
#   "k": 3
# }

#

import heapq

def sortKSortedArray(array, k):    
    # Write your code here.    
    sortedIndex = 0    
    heap = array[sortedIndex : k + 1]    
    heapq.heapify(heap)        
    for i in range(k + 1, len(array)):                
        array[sortedIndex] = heapq.heappop(heap)        
        sortedIndex += 1        
        heapq.heappush(heap, array[i])    
    while len(heap) > 0:        
        array[sortedIndex] = heapq.heappop(heap)        
        sortedIndex += 1    
    return array


print(sortKSortedArray([3, 2, 1, 15, 14,8 , 5, 4, 7, 6, 5],3))