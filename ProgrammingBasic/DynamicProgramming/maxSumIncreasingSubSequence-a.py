def maxSumIncreasingSubsequence(array): 

    seqArray = [None for _ in array]
    output = [None for _ in array]
    maxSum = 0

    for i in range(len(array)):
        current = array[i]
        temp = 0
        tempSequence = -1

        for j in range(0,i):
            if array[i] > array[j]:
                if array[i] + output[j] > temp:
                    temp = array[i] + output[j]
                    tempSequence = j

        
        current = max(temp,current)
        maxSum = max(current, maxSum)
        output[i] = current
        seqArray[i] = tempSequence


   
    result = [maxSum,getSequence(output, maxSum, seqArray, array)]
    return result


def getSequence(output, maxSum, seqArray, array):

    indexOfMaxSum = output.index(maxSum)

    maxSumSequence = [array[indexOfMaxSum]]

    while indexOfMaxSum > 0:

        indexOfMaxSum = seqArray[indexOfMaxSum]
        maxSumSequence.append(array[indexOfMaxSum])

    maxSumSequence.sort()
    return maxSumSequence



        


array = [10, 70, 20, 30, 50, 11, 30]

#array = [8, 12, 2, 3, 15, 5, 7]

print(maxSumIncreasingSubsequence(array))