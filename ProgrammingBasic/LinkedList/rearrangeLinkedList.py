# This is the class of the input linked list.
#6 -> 0 -> 5 -> 2 -> 1 -> 4 
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def rearrangeLinkedList(head, k):
    if head.next is None:
        return head
    some_value = None
    previous = head
    current = head.next
    while current is not None:
        if previous.value < k and current.value < k:
            some_value = current
            temp = current
            current = current.next
            previous = temp
            continue

        if previous.value < k and current.value >= k:
            some_value = previous
            temp = current
            current = current.next
            previous = temp
            continue

        if previous.value >= k and current.value >= k:
            temp = current
            current = current.next
            previous = temp
            continue

        if current.value <= k:
            temp = current
            previous.next = current.next
            current = current.next
            if some_value is None:
                head = temp
                head.next = previous
                some_value = head
            else:
                second_temp = some_value.next
                some_value.next = temp
                temp.next = second_temp
                some_value = some_value.next

            

            continue


        
			
ll = LinkedList(3)
ll.next = LinkedList(0)
ll.next.next  = LinkedList(2)
ll.next.next.next  = LinkedList(1)
ll.next.next.next.next  = LinkedList(4)
ll.next.next.next.next.next  = LinkedList(5)		
		
		
rearrangeLinkedList(ll,4)
