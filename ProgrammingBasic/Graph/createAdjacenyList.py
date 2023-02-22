def createAdjacency(array):
    adjacencyList  = {}
    for edge in array:
        if edge[0] not in adjacencyList:
            adjacencyList[edge[0]] = [edge[1]]
        else:
            adjacencyList[edge[0]].append(edge[1])


        if edge[1] not in adjacencyList:
            adjacencyList[edge[1]] = [edge[0]]
        else:
             adjacencyList[edge[1]].append(edge[0])

    print(adjacencyList)

array = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]

createAdjacency(array)