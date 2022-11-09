def kadanesAlgorithm(array):
    sumLeft, sumRight, left, start = 0, 0, 0, 0
    right, end = len(array)-1, len(array)-1

    while  left < right:
        sumRight+= array[right]
        if sumRight < 1:
            sumRight = 0
            start = right + 1

        
        sumLeft += array[left]
        if sumLeft < 1:
            sumLeft = 0
            end = left - 1

        
        right -= 1
        left += 1

    

    return sumLeft + sumRight
        
        

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
