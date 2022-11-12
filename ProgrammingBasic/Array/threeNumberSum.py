def threeNumberSum(array,sum):
    array.sort()
    arrayLen = len(array)
    output =[]

    for idx in range(arrayLen):
        firstElement = idx

        left = idx + 1
        right = arrayLen - 1 

        while (left < right):

            currentSum = array[firstElement] + array[left] + array[right]
            if currentSum == sum:
                output.append([array[firstElement],array[left],array[right]])
                left += 1
                right -= 1
            elif currentSum < sum:
                left += 1
            else:
                right -= 1

    return output
            


        
