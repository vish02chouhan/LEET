def boggleBoard(board, words):
    setOfWOrds = set(words)
    #print(setOfWOrds)
    result = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            dfs(row, col, board, setOfWOrds, result, words)
    print(list(result))       
    return list(result)
                
                
def dfs(row, col, board, setOfWOrds, result, words):
    stack = [[row,col]]
    stackChar =[]
    lastStackedData = {}
    visited = set()
    currentWord = ''
    while stack:
        cRow,cCol = stack.pop(0)
       
        char = board[cRow][cCol]
        probableWord = currentWord + char
    
        if probableWord in setOfWOrds and probableWord not in result:
            result.add(probableWord)
            break
            
        if checkCharacterInWords(probableWord, words):
            visited.add(f'{cRow}:{cCol}')
            lastStackedData[currentWord] = stack
            stack = []
            currentWord = probableWord
            neighbours = findNeighbours(cRow, cCol, board, visited)
            for neighbour in neighbours:
                stackChar.append(board[neighbour[0]][neighbour[1]])
                stack.append(neighbour)
        
def checkCharacterInWords(char, words):
    for word in words:
        if word.startswith(char):
            return True
        
    return False
    

def findNeighbours(row, col, board, visited):
    neighbourArray = []
    neighbourCells = [[row-1,col-1],[row-1,col],[row-1,col+1],[row,col+1], [row+1,col+1],[row+1,col],[row+1,col-1],[row,col-1]]
    for r,c in neighbourCells:
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and f"{r}:{c}" not in visited:
            neighbourArray.append([r,c])

    return neighbourArray



board = [
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"]
]

words = ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]
boggleBoard(board, words)