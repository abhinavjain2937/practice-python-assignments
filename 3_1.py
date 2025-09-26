

class Node:
    def __init__(self,data,next = None) -> None:
        self.data = data
        self.next = next
def insertion(head:Node,value:int):
    current = head
    new = Node(value)
    new.next = current
    head = new
    return head

def print_new(head):
    while head:
        print (head.data,end = "->")
        head = head.next

linked = Node(2,Node(3,Node(4,Node(5))))
fine = insertion(linked,1)
print(print_new(fine))



