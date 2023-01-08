def canSumA(sum, array):

    if sum == 0:
        return True
    
    if sum < 0:
        return False

    
    for number in array:
        remaining  = sum - number
        result = canSumA(remaining, array)
        if result:
            break

    return result

print(canSumA(7,[2,3,5,7]))