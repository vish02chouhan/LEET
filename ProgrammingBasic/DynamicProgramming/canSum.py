def canSum(sum, array, memo = {}):
    if sum in memo:
        return False
    if sum == 0:
        return True
    
    if sum < 0:
        return False
    
    for item in array:
        remainder = sum - item
        result = canSum(remainder, array)
        if not result:
            memo[remainder] = False
        if result:
            return True

    return False

print(canSum(7,[2,3,5,7]))