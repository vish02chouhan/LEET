def getPermutations(array):   
    permutations = [] 
    getPermutationHelper(array, [], permutations)
    return permutations

def getPermutationHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1 :]
            newPermutation = currentPermutation + [array[i]]
            getPermutationHelper(newArray, newPermutation, permutations)

print(getPermutations([1,2,3]))