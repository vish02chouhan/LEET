def longestPeak(array):
    mid = 1

    peakSize = 0
    currentPeakSize = 0
    while mid < len(array) -1:
        start = mid -1
        end  = mid + 1
        if array[mid] > array[start] and array[mid] > array[end]:
                #mid = 6
                #length =  13
                currentPeakSize = 3
                #print(mid)
                #mid =  12
                while start - 1 >= 0 and array[start] > array[start -1]:
                    currentPeakSize += 1
                    start -= 1

                while end + 1 < len(array) and array[end] > array[end+1]:
                        currentPeakSize += 1
                        end += 1
                mid += 1
                print(currentPeakSize)
                peakSize  = max(peakSize,currentPeakSize)
              
        else:
                mid += 1

    return currentPeakSize 
    

print(longestPeak( [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]))

    
