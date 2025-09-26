

class Node:
    def __init__(self,data,next = None) -> None:
        self.data = data
        self.next = next
def reverse(head: Node) -> Node:
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

# Create linked list
linked_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Reverse the list
rev = reverse(linked_1)

# Traverse both lists and find max sum of corresponding nodes
count = 0
original = reverse(rev)  # Re-reverse to restore original
while original and rev:
    add = original.data + rev.data
    count = max(count, add)
    original = original.next
    rev = rev.next

print(f"The maximum sum of corresponding nodes is: {count}")