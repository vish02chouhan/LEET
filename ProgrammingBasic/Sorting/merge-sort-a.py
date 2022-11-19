
def mergeSort(array):
	if len(array) == 1:
		return array
	arrayMedian = len(array)//2
	arr1 = array[:arrayMedian]
	arr2 = array[arrayMedian:]
	
	sa1 = mergeSort(arr1)
	sa2 = mergeSort(arr2)
	
	return mergeSortedArray(sa1,sa2)


def mergeSortedArray(arr1, arr2):
    left = 0
    right = 0
    outputArray = []

    while left < len(arr1) and right < len(arr2):
        if arr1[left][0] <= arr2[right][0]:
            outputArray.append(arr1[left])
            left += 1
        else:
            outputArray.append(arr2[right])
            right +=1

    while left < len(arr1):
        outputArray.append(arr1[left])
        left += 1

    while right< len(arr2):
        outputArray.append(arr2[right])
        right += 1

    return outputArray
    
def mergeOverlappingIntervals(array):
    sortedArray = mergeSort(array)
    output = []
    left = 0
    right = 1
    

    while right < len(sortedArray):

        if sortedArray[right][0] >= sorted[left][1]  and  sortedArray[right][1] <= sortedArray[left][1]:
           arr = sortedArray[left]
           arr[1] =  sortedArray[right][1] 
           right += 1
        else:
            output.append(sortedArray[left])
            left += 1
            right += 1









print(mergeOverlappingIntervals([[1, 2],[3, 5],[-3, -2],[6, 8],[-9, -3]]))