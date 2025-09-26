


class Node:
    def __init__(self,data,next = None) -> None:
        self.data = data
        self.next = next

def merger (list1:Node,list2:Node):
    
    current1 = list1
    next1 = None
    current2 = list2
    next2 = None
    if current1 == None and current2 == None:
        return list1
    while current1 and current2:
        if current1.data == current2.data or current1.data < current2.data:
            next1 = current1.next
            next2 = current2.next
            current1.next = current2
            current2.next = next1
            current1 = next1
            current2 = next2
        else:
            next1 = current1.next
            next2 = current2.next
            current2.next = current1
            current1.next = next1
            current1 = next1
            current2 = next2
    return list1


linked_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
linked_2 = Node(1, Node(2, Node(4, Node(5, Node(9)))))
mer = merger(list1=linked_1,list2=linked_2)

while mer:
    print(mer.data,end ="->")
    mer = mer.next


