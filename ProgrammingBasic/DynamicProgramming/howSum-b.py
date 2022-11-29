def howSum(sum, array, output = [],item = None):
    if sum == 0:
        return True,output

    if sum < 0:
        if len(output) > 0:
            output.pop()
        return False,output

    for item in array:
        remainder = sum - item
        output.append(item)
        (result, output) = howSum(remainder,array, output, item)
        #if result == False and len(output) > 0:
            #output.pop()


    return False,output

print(howSum(7,[2,3,5,7]))
