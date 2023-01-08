def hasSingleCycle(array):

    trackingArray = [0 for _ in array]
    lengthOfArray = len(array)

    left = 0
    counter = lengthOfArray
    result = False
    while counter >= 0:

        if trackingArray[left] > 1:
            break
            
        counter -= 1

        jump = array[left]
        left =  left + jump 
        if left < 0:
            left = lengthOfArray - left
        elif left >= lengthOfArray:
            left = left - lengthOfArray - 1
            
    return result

        
