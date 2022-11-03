

from itertools import count


array = [8,5,2]
#length of array is 7

def mergeSort(array):
    arrayLength = len(array)
    if arrayLength == 1:
        return array
    median = arrayLength//2
    array1 = mergeSort(array[:median])
    array2 = mergeSort(array[median:])

    finalArray = mergeSortedArray(array1, array2)
    return finalArray

def mergeSortedArray(array1, array2):

    array1Pointer = 0
    array2Pointer = 0
    
    array1Length = len(array1)
    array2Length = len(array2)

    sumOfArrays = array1Length + array2Length

    mergedArray = []

    for index in range(0,sumOfArrays):
 
        if array1Pointer >= array1Length and array2Pointer < array2Length:
            mergedArray.append(array2[array2Pointer])
            array2Pointer +=1
            continue
        elif array2Pointer >= array2Length and array1Pointer < array1Length:
            mergedArray.append(array1[array1Pointer])
            array1Pointer +=1
            continue

        if array1[array1Pointer] < array2[array2Pointer]:
            mergedArray.append(array1[array1Pointer])
            array1Pointer += 1
        else:
            mergedArray.append(array2[array2Pointer])
            array2Pointer += 1

    return mergedArray

print(mergeSort([2,4,6,1,3,5]))

##print(mergeSortedArray([],[1,3,5]))

