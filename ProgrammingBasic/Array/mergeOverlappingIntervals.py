def mergeOverlappingIntervals(arr):



    sortedArray = sorted(arr, key = lambda x:x[0])
    left = 0 
    right = 1
    while right < len(sortedArray)-1:
        if sortedArray[left][1] >= sortedArray[right][0] and sortedArray[left][1] <= sortedArray[right][1]:
            sortedArray[left][1] = sortedArray[right][1]
            del sortedArray[right]
            right +=1
        else:
            left += 1
            right += 1

    print(sortedArray)




array = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
  ]


mergeOverlappingIntervals(array)