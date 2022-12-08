# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


node = Node(1,None,None,None)



node.next = Node(2, node,None,None)

secondNode = node.next

secondNode.next = Node(3, secondNode, None, None)

thirdNode = secondNode.next

thirdNode.next = Node(4, thirdNode, None, None)

fourthNode = thirdNode.next

fourthNode.next = Node(5, fourthNode, None, None)

thirdNode.child = Node(7, None, None, None)

seventhNode = thirdNode.child

seventhNode.next = Node(8, seventhNode, None, None)

eightNode = seventhNode.next 

eightNode.child = Node(11, eightNode, None, None)

eightNode.next = Node(9,eightNode, None, None)



class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        stack = [head]
        last = None
        while stack:
            currentHead = stack.pop()
            if last and currentHead:
                last.next = currentHead
                currentHead.prev = last
            last = self.flattenHelper(currentHead, stack)
        return head


    def flattenHelper(self, head, stack = []):
        #1       
        current = head
        last = None
        
        while current is not None:
            if current.next is None:
                last = current
            # will reach 3
            if current.child is None:
                current = current.next
            else:

                if current.next is not None:
                    #[4]
                    stack.append(current.next)
                #current is 3, next 7
                current.next = current.child
                current.child = None
                current.next.prev = current
                current = current.next
        
        return last





sol = Solution()

sol.flatten(node)

a = 1