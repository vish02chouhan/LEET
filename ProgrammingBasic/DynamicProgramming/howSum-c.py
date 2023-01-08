def howSum(sum, array, output):

    if sum == 0:
        return []
    
    if sum < 0:
        return None

    
    for number in array:
        remaining = sum - number

        result = howSum(remaining, array, output)

        if result is not None:
            output.append(number)
            return output
            
    
    return None



output = []
print(howSum(7,[2,3,5,7], output))

print(output)
