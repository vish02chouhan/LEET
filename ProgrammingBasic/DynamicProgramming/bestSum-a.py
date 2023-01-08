def bestSum(sum, array):

    if sum == 0:
        return []
    
    if sum < 0:
        return None
    
    currentSum = None
    for item in array:
        remainder = sum - item
        result = bestSum(remainder, array)

        if result is not None:
           result.append(item)
           if currentSum is None or len(currentSum) > len(result):
                currentSum = result


    return currentSum

print(bestSum(7,[2,3,5,7]))