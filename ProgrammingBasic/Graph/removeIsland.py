def removeIslands(matrix):
    
    visited = [[False for value in row] for row in matrix]
    for i in range(0, len(matrix)):
        if i == 0 or i== len(matrix)-1:
            for j in range(len(matrix[i])):
                markVisitedToBoundryAndAdjacent1(i,j,matrix,visited)
        else:
                markVisitedToBoundryAndAdjacent1(i,0,matrix,visited)
                markVisitedToBoundryAndAdjacent1(i,len(matrix[i])-1,matrix,visited)
    for i in range(1, len(matrix)-1):
        for j in range(1,len(matrix[i])-1):
            if not visited[i][j] and matrix[i][j] == 1:
                matrix[i][j] = 0
    return matrix


def markVisitedToBoundryAndAdjacent1(i,j,matrix,visited):
    nodesToExplore =[[i,j]]

    while nodesToExplore:
        currentNode = nodesToExplore.pop()
        currentNodeI = currentNode[0]
        currentNodeJ = currentNode[1]

        #print( currentNodeI)
        print( "J:"+ str(currentNodeJ))

        if visited[currentNodeI][currentNodeJ]:
            continue
        
        visited[currentNodeI][currentNodeJ] = True

        if matrix[currentNodeI][currentNodeJ] == 0:
            continue

        unVisitedNeighbourArray = findNeighbour(currentNodeI, currentNodeJ, matrix, visited) 

        for item in unVisitedNeighbourArray:
            nodesToExplore.append(item)

        


def findNeighbour(i,j, matrix, visited):
    unVisitedNeighbourArray = []
    if i > 0 and not visited[i-1][j]:
        unVisitedNeighbourArray.append([i-1,j])
    if i < len(matrix)-1 and not visited[i+1][j]:
        unVisitedNeighbourArray.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unVisitedNeighbourArray.append([i,j-1])
    if j < len(matrix[i])-1 and not visited[i][j+1]:
        unVisitedNeighbourArray.append([i,j+1])

    return unVisitedNeighbourArray



array = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]

array1 =[
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1]
]

print(removeIslands(array1))