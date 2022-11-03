


def riverSizes(matrix):
    sizes = []

    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseMatrix(i,j,matrix,visited,sizes)

    return sizes


def traverseMatrix(i,j,matrix,visited, sizes):
    unvisitedArray = []
    size = 0
    unvisitedArray.append([i,j])

    while unvisitedArray:
        currentUnvisited = unvisitedArray.pop(0)
    
        if visited[currentUnvisited[0]][currentUnvisited[1]]:
            continue

        visited[currentUnvisited[0]][currentUnvisited[1]] = True
        if matrix[currentUnvisited[0]][currentUnvisited[1]]==0:
            continue

        size +=1
        unvisitedNeighboursArray = getUnvisitedNeighbours(currentUnvisited[0],currentUnvisited[1],matrix,visited)

        for item in unvisitedNeighboursArray:
            unvisitedArray.append(item)
    if size > 0:
        sizes.append(size)


def getUnvisitedNeighbours(i,j,matrix,visited):
    unvisitedNeighboursArray = []

    if i > 0 and not visited[i-1][j]:
        unvisitedNeighboursArray.append([i-1,j])
    if i < len(matrix)-1 and not visited[i+1][j]:
          unvisitedNeighboursArray.append([i+1, j])

    if j > 0 and not visited[i][j-1]:
        unvisitedNeighboursArray.append([i,j-1])
    if j < len(matrix[i][j])-1 and not visited[i][j+1]:
          unvisitedNeighboursArray.append([i, j+1])

    return unvisitedNeighboursArray


array = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]


array1 =[[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]

print(riverSizes(array1))