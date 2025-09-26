
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
def last_second(head:Node):
    if not head or not head.next:
        return None 
    current = head
    while current:
        if current.next.next == None:
            return current.data
        else:
            current = current.next
def print_list(head: Node | None):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print(" -> NULL")

list1 =Node(2, Node(3, Node(4, Node(5))))
val = last_second(list1)
print(val)