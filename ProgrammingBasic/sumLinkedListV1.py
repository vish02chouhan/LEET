from tkinter.messagebox import NO
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    l1 = ListNode(2,None)
    l1.next = ListNode(4,None)
    l1.next.next = ListNode(3,None)

    l2 = ListNode(5,None)
    l2.next = ListNode(6,None)
    l2.next.next = ListNode(4,None)

    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Current = l1
        l2Current = l2
        finalArray = None
        finalArrayCurrent = None
  
        carryOn:int = 0
        while l1Current != None or l2Current != None:

            currentValue = carryOn

            if l1Current != None :
                currentValue += l1Current.val
                l1Current = l1Current.next
            
            if l2Current != None:
                currentValue += l2Current.val
                l2Current = l2Current.next  
            
            carryOn = 0
            if currentValue > 9:
                if finalArray == None:
                    finalArray = ListNode(currentValue%10, None)
                    finalArrayCurrent = finalArray
                else:
                    finalArrayCurrent.next = ListNode(currentValue%10, None)
                    finalArrayCurrent = finalArrayCurrent.next
                carryOn = int(currentValue / 10)
                print(carryOn)
            else:
                if finalArray == None:
                    finalArray = ListNode(currentValue, None)
                    finalArrayCurrent = finalArray
                else:
                    finalArrayCurrent.next = ListNode(currentValue, None)
                    finalArrayCurrent = finalArrayCurrent.next

            
            if carryOn > 0:
                finalArrayCurrent.next = ListNode(carryOn, None)


        return finalArray
    

              
    print(addTwoNumbers(l1,l2))
