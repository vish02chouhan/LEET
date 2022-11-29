def removeIslands(matrix):
    visitedArray = [[False for _ in row]for row in matrix]





def visitAdjacentArray(i,j,matrix, visitedArray):

    nodesToVisit = [[i,j]]

    while nodesToVisit:
        currentNode = nodesToVisit.pop()
        if visitedArray [currentNode[0]][currentNode[1]]:
            continue
        visitedArray[currentNode[0]][currentNode[1]] = True

        if visitedArray [currentNode[0]][currentNode[1]] == 1:
            continue


def getNeighbourNode():



























    pass



matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]