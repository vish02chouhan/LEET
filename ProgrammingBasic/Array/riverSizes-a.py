def riverSizes(matrix):
    visited = [[False for _ in row]for row in matrix]
    print(visited)
    result = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col] and matrix[row][col] == 1:
                riverSize = processNeighbour(row, col, matrix, visited)
                result.append(riverSize)

    return result


def processNeighbour(row, col, matrix, visited):
  nodeToProcess =[[row,col]]
  riverSize = 0
  while nodeToProcess:
    currentNode = nodeToProcess.pop()
    currentRow = currentNode[0]
    currentColumn = currentNode[1]

    if matrix[currentRow][currentColumn] == 0 or visited[currentRow][currentColumn]:
        continue

    if matrix[currentRow][currentColumn] == 1:
        riverSize += 1

    visited[currentRow][currentColumn] = True

    getNeightbour(currentRow, currentColumn, matrix, visited,nodeToProcess)

  return riverSize
    
    
def getNeightbour(row, col, matrix, visited,nodeToProcess):

  if row + 1 < len(matrix) and not visited[row+1][col]:
      nodeToProcess.append([row+1,col])

  if row > 0 and not visited[row-1][col]:
      nodeToProcess.append([row - 1,col])
  
  if col + 1 < len(matrix[row])  and not visited[row][col+1]:
      nodeToProcess.append([row,col+1])

  if col > 0 and not visited[row][col-1]:
      nodeToProcess.append([row,col-1])


    

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]

print(riverSizes(matrix))