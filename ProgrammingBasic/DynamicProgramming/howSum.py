def howSum(sum, array, output = []):

    if sum == 0:
        return (True,output)
    
    if sum < 0:
        return (False,[])
    
    for item in array:
        remainder = sum - item
        (result,output) = howSum(remainder,array, output)
        print(output)
        if result:
            output.append(item)
            return (True, output)

    return (False,output)

print(canSum(7,[2,3,5,7]))
