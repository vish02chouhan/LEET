def powerset(array):
    if len(array) == 0:
        return [[]]
    
    if len(array) == 1:
        return [[],array]

    subsets = [[]]
  
    for idx,item in enumerate(array):
        subsets.append([item])
        innerArray = array[idx+1:]
        for iitem in innerArray:
            nextItem = [item,iitem]
            subsets.append(nextItem)
    subsets.append(array)

    return subsets


print(powerset([1]))