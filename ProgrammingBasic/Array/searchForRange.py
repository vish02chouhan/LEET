def searchForRange(array, target):

    index = binarySearch(array,0,len(array))

    if index == -1:
        return [-1,-1]

    minIndex = index
    maxIndex = index
    left = index - 1 
    right = index + 1

    while left > 0 or right < len(array)-1:

      if array[left] == target:
          left -= 1

      if array[right] == target:
          right += 1

      if array[left] != target and array[right] != target:
          break

    return [left,right]



def binarySearch(array, left, right, target):

    if left > right:
        return -1

    median = right//2

    if array[median] == target:
        return target

    if array[median] > target:
       right = median - 1
    else:
        left = median + 1

    return binarySearch(array, left, right, target)
      

    
    
