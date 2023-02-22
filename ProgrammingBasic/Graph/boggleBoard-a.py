def boggleBoard(board, words):
    setOfWOrds = set(words)
    #print(setOfWOrds)
    result = set()
   
    for row in range(len(board)):
        for col in range(len(board[row])):
            visited = set()
            explore(row, col, board, setOfWOrds, board[row][col], result, visited)
    print(result)
    return list(result)
                
def explore(row, col, board, setOfWOrds, word, result, visited):
    if word in setOfWOrds:
        result.add(word)
        return True

    if not checkCharacterInWords(word, setOfWOrds):
        return False

    visited.add(f"{row}:{col}")

    neighbours = findNeighbours(row, col, board, visited)

    for neighbour in neighbours:
        newWord = word + board[neighbour[0]][neighbour[1]]
        explore(neighbour[0], neighbour[1], board, setOfWOrds, newWord, result, visited )

        
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