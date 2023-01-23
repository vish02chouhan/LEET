def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1




firstDuplicateValue([2, 1, 5, 2, 3, 3, 20])