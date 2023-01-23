#squarematrix r =0 , c= 2
# r = 0, c = 0 - 8
# r = 0 to 8,  c = 0
# For sub matrix we need to check - 
# r = 0 , c = 0 - 2
# r = 0-2 , c = 0
# r // 3 * 3 to r // 3 * 3 + 2 -> 
# r = 0 -> 0 to 2
# r = 1 -> 0 to 2 
# r = 2 -> 0 to 2
# r = 3 -> 3 to 5
# r = 4 -> 3 to 5
# r = 6 -> 6 to 8

def checkValueSubMatrix(r,c,n, board):
    startRow = r//3 * 3
    endRow = startRow + 2
    startCol = c//3 * 3
    endCol = startCol + 3
    for row in range(startRow, endRow):
        for col in range(startCol, endCol):
            if board[row][col] == n: return False

    return True


def checkValue(r,c,n, board):
    if checkValueSubMatrix():
        for i in range(9):
            if board[r][i] == n: return False
            if board[i][c] == n: return False
        return True
    
    return False


def solveSudoku(board):

    for row in range(board):
        for col in range(board[row]):

            if board[row][col] != 0: continue
            for i in range(1,10):
                if checkValue(row, col, i,board):
                    board[row][col] = i
                    if solveSudoku(board):
                        return True
                    board[row][col] = 0



    pass


