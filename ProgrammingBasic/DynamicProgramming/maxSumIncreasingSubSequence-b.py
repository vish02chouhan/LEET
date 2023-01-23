def maxSumIncreasingSubsequence(array):
    sums = [0] * len(array)
    sequence =[None] * len(array)
    sums[0] = array[0]

    maxSum = 0
    maxSumIndex = 0

    for i in range(1, len(array)):
        for j in range(i-1,-1,-1):
            if array[j] < array[i]:
                sums[i] = sums[j] + array[i]
                if sums[i] > maxSum:
                    maxSum = sums[i]
                    maxSumIndex = i
                maxSum = max(maxSum, sums[i])
                sequence[i] = j
                break
    
    print(maxSumIndex)
    print(maxSum)
    print(sequence)
    return [maxSum, buildSequence(maxSumIndex, sequence,array)]


def buildSequence(maxId, sequence, array):
    sequenceArray = []
    sequenceArray.append(array[maxId])
    currentId = sequence[maxId]
    #currentId  = 4
    while currentId != None:
        #currentId 4,3,2,0
        #itemIndex = 3,2,0,-1

        sequenceArray.append(array[currentId])
        currentId = sequence[currentId]
        
    return sequenceArray


        


array = [10, 70, 20, 30, 50, 11, 30]

#array = [8, 12, 2, 3, 15, 5, 7]

print(maxSumIncreasingSubsequence(array))