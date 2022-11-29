edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
    
]

def createAdjacencyList():
    currentDist = {}
    for item in edges:
        if item[0] not in currentDist:
            currentDist[item[0]] = [item[1]]
        else:
            currentDist[item[0]].append(item[1])

        if item[1] not in currentDist:
            currentDist[item[1]] = [item[0]]
        else:
            currentDist[item[1]].append(item[0])

    print(currentDist)


createAdjacencyList()