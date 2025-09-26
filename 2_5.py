class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Helper function to reverse the list (from a previous problem)
def reverse_list(head: Node | None) -> Node | None:
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

# The main function to add one
def add_one(head: Node | None) -> Node | None:
    # 1. Reverse the list
    head = reverse_list(head)
    
    current = head
    carry = 1 # Start with a carry of 1 to perform the addition

    while current and carry > 0:
        # Add the carry to the current node's data
        current.data += carry
        
        # If the sum is less than 10, we are done
        if current.data < 10:
            carry = 0
        # Otherwise, update the data and continue with the carry
        else:
            current.data = 0
            carry = 1
        
        # Move to the next node if we haven't processed the whole list yet
        if not current.next and carry > 0:
            # This handles the case like 9->9->9 becoming 1->0->0->0
            current.next = Node(1)
            carry = 0

        current = current.next

    # 3. Reverse the list back to its original order and return it
    return reverse_list(head)

def print_list(head: Node | None):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print(" -> NULL")

list1 = Node(1, Node(9, Node(9, Node(9))))
print("Original list:")
print_list(list1)

result1 = add_one(list1)

print("\nList after adding 1:")
print_list(result1) 

print("-" * 20)

