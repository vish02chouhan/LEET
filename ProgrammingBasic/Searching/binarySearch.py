

def binarySearchV1(array, target):
    if len(array) <=0:
        return False

    mid = len(array)//2

    if array[mid] == target:
        return True
    
    if array[mid] > target:
        return binarySearchV1(array[:mid],target)
    else:
        return binarySearchV1(array[mid+1:], target)



#print(binarySearchV1([99, 100, 103, 106, 128, 1004],6))


def binarySearch(array, target, left, right):
    if len(array) == 0:
        return -1

    
    mid =  (left+ right)//2 # 1 = 2

    # array[mid]  is 103
    if array[mid] == target:
        return mid
    
    
    if array[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
    
    # as 103 is greater than 99
    # left = 0
    return binarySearch(array, target, left,right)



print(binarySearch([99, 100, 103, 106, 128, 1004],99,0,5))


