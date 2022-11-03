# Definition for singly-linked list.
from locale import currency
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self,data):
        if self.head == None:
            self.head = ListNode(data)
            return        
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = ListNode(data)


    def length(self):
        cur = self.head

        total = 0
        if cur == None:
            return 0
        
        while cur != None:
            cur = cur.next
            total +=1

        return total

    def display(self):
        cur = self.head
        if self.head == None:
            return "No Element Exists"

        while cur != None:
            print(cur.val)
            cur = cur.next        



def addLinkedListItem():
    linkedList = LinkedList()
    print('Adding')
    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(2)
    linkedList.append(1)

    linkedList.display()
    print(linkedList.length())

def isPalindrome(head: Optional[ListNode]) -> bool:
    if head == None:
        return False

    currentElement = head
    
    while currentElement.next != None:
        print(head.val)

    
addLinkedListItem()