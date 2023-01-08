
def solveSudoku(board):

	backtrack(board)
	return board


def valid_move(r, c, n, board):
	for i in range(9):
		if board[i][c]==n: return False
		if board[r][i]==n: return False
		if board[3*(r//3)+i//3][3*(c//3)+i%3]==n: return False
	return True

def backtrack(board):

	for r in range(9):
		for c in range(9):
			if board[r][c]!=0: continue
			for n in [int(i) for i in "123456789"]:
				if valid_move(r, c, n,board):
					board[r][c] = n
					if backtrack(board): return True
					board[r][c] = 0
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