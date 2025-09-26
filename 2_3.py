class Node:
    
    def __init__(self,data,next = None) -> None:
        self.data = data 
        self.next = next
        

def list_fun (head:Node)->Node:
    """ the value given is always assending order
    """
    current = head
    # If the list is empty, there's nothing to do.
    if not head:
        return None
    while current and current.next:
        if  current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

def print_list(head: Node):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")

head_1 = Node(11,Node(11,Node(11,Node(12,Node(12,Node(14,Node(14,Node(15,Node(16)))))))))

list_fun(head_1)

print_list(head_1)