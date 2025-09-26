
class Node:
    
    def __init__(self,data,next = None) -> None:
        self.data = data 
        self.next = next

def reversal_linked_list(head:Node):
    if not head:
        return
    previous = None
    current = head
    next = None

    while current :
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous
def print_list(head:Node|None):
    current = head
    while current:
        print(current.data,end=' -> ')
        current = current.next

list1 =Node(2, Node(3, Node(4, Node(5))))
lkj = reversal_linked_list(list1)
print("_____________________________________")
print_list(lkj)



