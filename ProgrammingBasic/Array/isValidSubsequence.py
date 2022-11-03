def isValidSubsequence(array, sequence):
    sequenceIndex = []
    lastIndex = 0
    for idx,item in enumerate(sequence):
        try:
          
            if len(sequenceIndex) > 0:
                lastIndex = sequenceIndex[len(sequenceIndex) - 1] + 1
            index = array[lastIndex:].index(item)
            sequenceIndex.append(index)
        except ValueError as ve:
            return False

    print(sequenceIndex)

    for x in range(len(sequenceIndex)-1):
        if sequenceIndex[x] >= sequenceIndex [x+1]:
            return False

    return True
 
array = [1, 1, 1, 2, 1]
sequence = [1, 1, 1]

print(array[1:].index(1))




print(isValidSubsequence(array, sequence))
