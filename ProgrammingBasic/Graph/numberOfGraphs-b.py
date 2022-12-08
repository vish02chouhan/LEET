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
  
    visited  = set()
    sum = 0
    for key in graph:
        if key in visited:
            continue

        nodeToVisit = [key]
        while nodeToVisit:
            currentNode = nodeToVisit.pop()

            if currentNode in visited:
                continue

            visited.add(currentNode)

            for childern in graph[currentNode]:
                nodeToVisit.append(childern)
                
        print(visited)
        sum += 1

    print(sum)


numberOfGraphs(graph)