def nextGreaterElement(array):
    result = [float('inf')] * len(array)

    left = 0
    right = 1
    while left < len(array):

        if right > len(array)-1:
            right = 0

        if right == left:
            result[left] = -1
            left += 1
            right = left + 1


        if array[left] > array[right]:
            right += 1
        else:
            result[left] = array[right]
            left += 1
            right = left + 1




        print(result)
        print(left)
        print(right)

    return result


print(nextGreaterElement([6, 4, 5, 7, 2, 1, 3]))