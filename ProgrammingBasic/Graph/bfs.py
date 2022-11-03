#Breadth first traversal

import queue


class Node:
    def __init__(self,name) -> None:
        self.name = name
        self.children = []
        pass

    def addChildren(self,name):
        self.children.append(Node(name))


    def bfs(self, array):
        queue.pu
