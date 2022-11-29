#Breadth first traversal

from collections import deque
import queue


class Node:
    def __init__(self) -> None:
        pass

    graph = {
        'a':['c','b'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'g':[],
        'h':[]
    }

    graph1 = {
        'a':['c','b'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'g':[],
        'h':[]
    }



    def dfs(self):
        source = ['a']
        output =[]
        queue = []

        while source:
           outputItem = source.pop()
           if not outputItem:
            continue

           output.append(outputItem)
           if outputItem  in self.graph:
            for item in self.graph[outputItem]:
                    source.append(item)


        return output
    
    def dfsRecursive(self, source):
        print(source) 

        if source in self.graph1:    
            for item in self.graph1[source]:
                self.dfsRecursive(item)


    def bfs(self):
        source = ['a']
        output =[]
        while source:
           outputItem = source.pop(0)
           if not outputItem:
            continue

           output.append(outputItem)
           if outputItem  in self.graph:
            for item in self.graph[outputItem]:
                    source.append(item)


        return output 

    def bfsType(self):
        source = deque()
        source.append('a')
        output =[]
        while source:
           outputItem = source.popleft()

           output.append(outputItem)
           if outputItem  in self.graph:
            for item in self.graph[outputItem]:
                    source.append(item)


        return output 


        
    

node =Node()

print(node.bfs())


#print(node.dfsRecursive('a'))







