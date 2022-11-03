from typing import List

from numpy import true_divide


class Node:

    def __init__(self, name):
        self.name = name
        self.children = []


def cycleInGraph(edges):
    nodeArray = []
    visited = [[False for x in row]for row in edges]

    for idx,item in enumerate(edges):
        nodeArray.append(Node(idx))

    for i in range(len(edges)):
        for j in edges[i]:
            nodeArray[i].children.append(nodeArray[j])
    
    return traverse(nodeArray[0],visited)
    # Write your code here.

def traverse(node, visited):
    unexploredNodes = []
    unexploredNodes.append(node)
    while unexploredNodes:
        currentNode = unexploredNodes.pop()
        i = currentNode.name
        for item in currentNode.children:
            j = item.name

            if visited[i][j]:
                return True
            else: 
                visited[i][j] = True
                unexploredNodes.append(item)
    return False

edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    []
  ]

cycleInGraph(edges)