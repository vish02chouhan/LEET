graph = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}

def largestComponent(graph):
    visitedNode = set()
    maxSize = 0
    for item in graph:
        size = explore(item, graph, visitedNode, 0)
        maxSize = max(size, maxSize)
        

    print(maxSize)

def explore(node, graph, visitedNode, count = 0):
    if node in visitedNode:
        return count

    count += 1
    visitedNode.add(node)

    for item in graph[node]:
        
       count = explore(item, graph, visitedNode, count)

    return count


largestComponent(graph)