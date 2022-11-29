def spiralTraverse(array):
    visitedArray = [[False for _ in row]for row in array]
    isProcessing =  True
    row = 0
    col = -1
    outPutArray = []
    while isProcessing:
        if row == 0 and col < len(array[row]) -1: # 3
            col += 1
            outPutArray.append(array[row][col])
            visitedArray[row][col] = True
            continue

        if col == len(array[row]) - 1 and row < len(array)-1 :
            row += 1
            outPutArray.append(array[row][col])
            visitedArray[row][col] = True
            continue

        if row == len(array) -1 and col > 0:
            col -= 1
            outPutArray.append(array[row][col])
            visitedArray[row][col] = True
            if col == 0:
                isProcessing = False
    
    isProcessing = True
    while isProcessing:
        
        if visitedArray[row-1][col] == False:
              outPutArray.append(array[row-1][col])
              visitedArray[row][col] = True
              row -= 1





    print(outPutArray)
        

        

        
            
    
  
  
  
  
array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]
spiralTraverse(array)
# create a visiArray and keep track of visited cells also
# 1) - i = 0,j = 0 -> increase j 
# 2) if j == len(array[i]) -- 3
# 3) increase i, if i == len(array) - j == 3 and i ==3
# 4) decrease j
# 5) if j == 0  i is 3 and j is 0
# 6) decrease i

traverse = [[0,0],[0,1],[0,2],[0,3], # i = 0, j = 0,1,2,3 if j =
            [1,3],[2,3],[3,3],
            [3,2],[3,1],[3,0],
            [2,0],[1,0],
            [1,1],[1,2],
            [2,2],
            [2,1]]


#increase width 
#increase height
#decrease weight
#decrease height

