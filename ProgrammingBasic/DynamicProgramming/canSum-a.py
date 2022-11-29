def canSumA(sum, array, resultArray=[]):

    if sum < 0:
        return (False,resultArray)
    
    if sum == 0:

        return True,resultArray

    
    for number in array:
        remainder = sum - number
        result, resultArray = canSumA(remainder, array, resultArray)
        if result:
            print(resultArray)
            resultArray.append(number)
            break

    return False, resultArray

print(canSumA(7,[2,3,5,7]))