graph = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}

def numberOfGraphs(graph):
    visitedNode = set()
    sum = 0
    for item in graph:
        if explore(item, graph, visitedNode):
            sum += 1

    print(sum)

def explore(node, graph, visitedNode):
    if node in visitedNode:
        return False

    visitedNode.add(node)

    for item in graph[node]:
        explore(item, graph, visitedNode)

    return True


numberOfGraphs(graph)