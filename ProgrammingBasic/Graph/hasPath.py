from collections import deque


graph = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i','k'],
    'k':[],
}

def hasPath(source, node):

    queue = deque()
    queue.append(source)

    while queue:
        currentNode = queue.popleft()

        if currentNode == node:
            return True

        for item in graph.get(currentNode):
            queue.append(item)


    return False



# def hasPath(source, node):
#     if source == node:
#         return True

#     if source in graph:
#         for item in graph[source]:
#             result = hasPath(item,node)
#             if result:
#                 return result

#     return False


print(hasPath('f','j'))