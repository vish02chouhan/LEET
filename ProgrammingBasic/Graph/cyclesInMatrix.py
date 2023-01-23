
from typing import List


def containsCycle(grid: List[List[str]]) -> bool:
    visited = [ [False for _ in row] for row in grid]
    result = False
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row > 0:
                result = dfs(row - 1, col, row,col,grid,grid[row][col])
                if result:
                    return result

            if row < len(grid)-1:
                result = dfs(row + 1, col, row,col,grid,grid[row][col])
                if result:
                    return result

            if col > 0:
                result = dfs(row, col - 1, row,col,grid,grid[row][col])
                if result:
                    return result
            
            if col < len(grid[row])-1:
                result = dfs(row, col + 1, row,col,grid,grid[row][col])
                if result:
                    return result
    return result


def dfs(row, col, startRow,startCol,grid,cycleValue, visited = set()):
    print(str(row)+':'+str(col))
    
    if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[row]) - 1:
        return False

    if row == startRow and col == startCol:
        return True
    
    if grid[row][col] != cycleValue:
        return False

    if str(row)+':' + str(col) in visited:
        return False

    visited.add(str(row)+':' + str(col))

    result = dfs(row - 1, col, startRow,startCol,grid,cycleValue)
    if result:
        return result
    result = dfs(row + 1, col, startRow,startCol,grid,cycleValue)
    if result:
        return result
    result = dfs(row, col + 1, startRow,startCol,grid,cycleValue)
    if result:
        return result
    result = dfs(row, col - 1, startRow,startCol,grid,cycleValue)

    return result


grid = [["a","b","b"],["b","z","b"],["b","b","a"]]

print(containsCycle(grid))
    