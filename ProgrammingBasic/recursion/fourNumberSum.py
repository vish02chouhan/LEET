def fourNumberSum(array, targetSum, currentSum = [], result = []):

    
    for idx in range(len(array)):
        currentTarget = targetSum - array[idx]
        if currentTarget == 0 and len(currentSum) == 3:
            #currentSum.append(array[idx])
            result.append(currentSum + [array[idx]])
        elif len(currentSum) < 3:
            newCurrentSum = currentSum + [array[idx]]
            newArray = array[idx+1:]
            fourNumberSum(newArray, currentTarget, newCurrentSum, result)


    return result

    
array = [7, 6, 4, -1, 1, 2]
print(fourNumberSum(array, 16))

