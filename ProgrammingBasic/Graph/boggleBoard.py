def boggleBoard(board, words):
    setOfWOrds = set(words)
    print(setOfWOrds)
    result = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            dfs(row, col, board, setOfWOrds, result, words)
            
    return result
                
                
def dfs(row, col, board, setOfWOrds, result, words):
    stack = [[row,col]]
    currentWord = ''
    probableWord = ''
    while stack:
        cRow,cCol = stack.pop(0)
        char = board[cRow][cCol]
        probableWord = currentWord + char
    
        if probableWord in setOfWOrds:
            result.append(probableWord)
            break
            
        if checkCharacterInWords(currentWord, words):
            currentWord = probableWord
            neighbours = findNeighbours(cRow, cCol, board)
            for neighbour in neighbours:
                stack.append(neighbour)

        
def checkCharacterInWords(char, words):
    for word in words:
        if word.startswith(char):
            return True
        
    return False
    

def findNeighbours(row, col, board):
    neighbourArray = []
    neighbourCells = [[row-1,col-1],[row-1,col],[row-1,col+1],[row,col+1], [row+1,col+1],[row+1,col],[row+1,col-1],[row,col-1]]
    for r,c in neighbourCells:
        if 0 <= r < len(board) and 0 <= c < len(board[0]):
            neighbourArray.append([r,c])

    return neighbourArray
