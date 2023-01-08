def howSum(sum, array, output = []):

    if sum == 0:
        return []
    
    if sum < 0:
        return None
    
    for item in array:
        remainder = sum - item
        result = howSum(remainder,array, output)
        if result is not None:
            result.append(item)
            return result

    return None

print(howSum(7,[2,3,5,7]))
