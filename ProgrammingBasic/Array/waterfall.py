class nodesInfo:
    def __init__(self,x,y,percentage):
        self.x = x
        self.y = y
        self.percentage = percentage

def waterfallStreams(array, source):
    bucketArray = []
    bucketNodeArray = []
    if array[1][source] == 1:
        for item in array[1][source]:
            bucketArray.append(0)
            return bucketArray
    
    visited = [[False for x in rows] for rows in array]

    nodeToVisitStack = []
    nodeToVisitStack.append(nodesInfo(1,source,100))
    visited[1][source] = True
    arrayLength = len(array)
    while nodeToVisitStack:
        currentNode = nodeToVisitStack.pop(0)
        x = currentNode.x
        if x == len(array)-1:
            bucketNodeArray.append(currentNode)
            continue

        y = currentNode.y
        per = currentNode.percentage


        if x+1 < arrayLength and array[x+1][y] == 0 and visited[x+1][y] == False:
            visited[x+1][y] = True
            nodeToVisitStack.append(nodesInfo(x+1,y,per))

        elif y > 0 and array[x][y-1] == 0 and y < len(array[x]) and array[x][y+1] == 0:
            if visited[x][y-1] == False and visited[x][y+1] == False:
                visited[x][y-1] = True
                visited[x][y+1] = True
                nodeToVisitStack.append(nodesInfo(x,y-1,per//2))
                nodeToVisitStack.append(nodesInfo(x,y+1,per//2))
            elif visited[x][y-1] == False and visited[x][y+1] == True:
                visited[x][y-1] = True
                nodeToVisitStack.append(nodesInfo(x,y-1,per))
            elif visited[x][y-1] == True and visited[x][y+1] == False:
                visited[x][y+1] = True
                nodeToVisitStack.append(nodesInfo(x,y+1,per))

        elif y > 0 and array[x][y-1] == 0 and y < len(array[x])-1 and array[x][y+1] != 0:
            if visited[x][y-1] == False:
                visited[x][y-1] = True
                nodeToVisitStack.append(nodesInfo(x,y-1,per))
        elif y > 0 and array[x][y-1] != 0 and y < len(array[x])-1 and array[x][y+1] == 0:
            if visited[x][y+1] == False:
                visited[x][y+1] = True
                nodeToVisitStack.append(nodesInfo(x,y+1,per))
    

    bucketIds = [item.y for item in bucketNodeArray]
    for idx,item in enumerate(array[x]):
        if idx in bucketIds:
            bucketArray.append([item.percentage for item in bucketNodeArray if item.y == idx][0])
        else:
            bucketArray.append(0)

    return bucketArray



            



array = [
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0]
]

array1 =[
    [0],
    [0],
    [0],
    [0],
    [0],
    [1],
    [0]
  ]

array2 = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
]

array3 = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]


array4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(waterfallStreams(array2,3))