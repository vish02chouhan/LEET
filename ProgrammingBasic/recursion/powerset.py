def powerset(array):
    powArray = [[]]
    for item in array:
        for iitem in range(len(powArray)):
            powArray.append([item] + powArray[iitem])


    return powArray


print(powerset([1,2,3]))