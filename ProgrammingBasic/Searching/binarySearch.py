# 0,1,2,3,4,5,6

array = [2,4,6,8,10, 11, 12]

print(array[4:6])

def binarySearch(array, target, index = 0):
    arrayLength = len(array)
    if arrayLength == 1:
        return index
    median = len(array)//2

    if array[median] == target:
        return median
    elif array[median] < target:
        binarySearch(array[median])
    else:
        binarySearch(array[:median])

    pass
