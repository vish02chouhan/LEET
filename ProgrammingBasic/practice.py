array = [75, 105, 120, 75, 90, 135]


def maxSubsetSumNoAdjacent(array):

    if not len(array):
        return 0 
    elif len(array) == 1:
        return array[O] 
    maxSums = array[:] 
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    return maxSums[-1]

def isPalindrome(string):
    length = len(string)
    for i in range(length//2):
        print(string[i])
        print(string[length-1-i])
        string[i] != string[length-1-i]
        return False

    return True


# print(isPalindrome('abcdcba'))


# print ("a" == "a")


print (3>(5 or 4))