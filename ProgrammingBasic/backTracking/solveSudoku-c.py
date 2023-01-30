def solveSudoku(board):

    backtrack = []
    backtrack1 = []
    helper(board,backtrack, backtrack1)
    print(', '.join(backtrack))
    print(', '.join(backtrack1))
    return board


def helper(board, backtrack, backtrack1):

  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] != 0:
        continue
      for value in range(1,10):
        if isValid(value, row, col, board):
          board[row][col] = value

          backtrack1.append(str(row)+":"+ str(col) +'='+ str(value))
         
          if helper(board, backtrack,backtrack1):
            return True

          backtrack.append(str(row)+":"+ str(col))
          board[row][col] = 0

      return False
  return True
            
        



def isValid(value, row, col, board):

    for rowId in range(0,9):
        if board[rowId][col] == value:
            return False

    for colId in range(0,9):
        if board[row][colId] == value:
            return False

    startRow = row - row%3
    startCol = col - col%3
    #0,1,2 - 3,4,5 - 6,7,8
    for rowId in range(startRow, startRow+3):
        for colId in range(startCol, startCol+3): 
            if board[rowId][colId] == value:
                return False

    return True
    
    

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
  ]

solveSudoku(board)
