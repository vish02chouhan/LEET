def hasSingleCycle(array):
    visited = [False] * len(array)
    count = 0
    index = 0

    while  count < len(array):
        #1) Visited[0] = False, 2)False 3) False
        #1) index = 0 2) 2 3) 3, 4) -1(4)
        
        index = index % len(array)

        if visited[index]:
            return False

        #1) Visited[0] = True 2) [2] = True, 3) [3] = True
        visited[index] = True
        #1) jump = 2, 2) 1 3) -4
        jump = array[index]
        #1) index = 2, 2) 3, 3) -1
        index += jump
        #1) count = 1 , 2) = 2 , 3) = 3
        count += 1

    print(count)
    print(visited)
    if index != 0:
        return False

  
    return True


hasSingleCycle([2, 3, 1, -4, -4, 2])
