graph = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}

sum = 0
visitedSet = set()
for item in graph:
    print(visitedSet)
    if item in visitedSet:
        continue
    graphNodesToVisit = [item]

    while graphNodesToVisit:
        node = graphNodesToVisit.pop()
        if node in graph.keys() and node not in visitedSet:
            visitedSet.add(node)
            for connectedNode in graph[node]:
                graphNodesToVisit.append(connectedNode)

    sum += 1

print(sum)

    




