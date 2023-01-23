def solve(grid):
  empty_cell = find_empty_cell(grid)
  if not empty_cell:
    return True  # Puzzle is solved
  row, col = empty_cell
  for number in range(1, 10):
    if is_valid_choice(grid, row, col, number):
      grid[row][col] = number
      if solve(grid):
        return True
      grid[row][col] = 0  # Reset the cell
  return False  # Puzzle is unsolvable



def find_empty_cell(grid):
  for row in range(9):
    for col in range(9):
      if grid[row][col] == 0:
        return (row, col)
  return None

def is_valid_choice(grid, row, col, number):
  # Check if the number is valid in the row
  if number in grid[row]:
    return False

  # Check if the number is valid in the column
  for i in range(9):
    if grid[i][col] == number:
      return False

  # Check if the number is valid in the 3x3 subgrid
  subgrid_row = row // 3
  subgrid_col = col // 3
  for i in range(3):
    for j in range(3):
      if grid[subgrid_row * 3 + i][subgrid_col * 3 + j] == number:
        return False
  return True

# Example usage
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if solve(grid):
  for row in grid:
    print(row)
else:
  print("No solution found.")
