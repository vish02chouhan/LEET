def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    leftArray = None
    rightArray = None
    if arrayOne[len(arrayOne) - 1] >= arrayTwo[0]: 
        leftArray = arrayOne
        rightArray = arrayTwo
    else:
        leftArray = arrayTwo
        rightArray = arrayOne


    left = len(leftArray) - 1
    right = 0

    dict = {}
    smallestKey = None
    smallestObject = None
    minDiff = float('inf')

    while left > 0:
        for idx in range(len(rightArray)):
            diff = abs(leftArray[left] - rightArray[idx])
            if diff < minDiff:
                minDiff = diff
            else:
                if smallestKey == None: 
                    smallestKey = minDiff       
                    smallestObject = [leftArray[left], rightArray[idx-1]]
                else:
                    if minDiff < smallestKey:
                        minDiff = smallestKey
                        smallestObject = [leftArray[left], rightArray[idx-1]]
                minDiff = float('inf')
                break
        
        left -= 1

    return smallestObject

  
print(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135,11, 15, 17]))