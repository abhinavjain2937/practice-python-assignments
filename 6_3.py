class Node:
    """A node in a singly linked list."""
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next_element = next

def create_linked_list(items: list) -> Node:
    """Helper function to convert a Python list to a linked list."""
    if not items:
        return None
    head = Node(items[0])
    current = head
    for item in items[1:]:
        current.next_element = Node(item)
        current = current.next_element
    return head

def print_linked_list(head: Node) -> None:
    """Helper function to print a linked list."""
    current = head
    result = []
    while current:
        result.append(str(current.data))
        current = current.next_element
    print(" -> ".join(result))

def addition(list1: Node, list2: Node) -> Node:
    '''Adds two numbers represented by linked lists in reverse order.'''
    dummy_head = Node(0)
    current = dummy_head
    carry = 0

    # Traverse both lists
    while list1 or list2 or carry:
        val1 = list1.data if list1 else 0
        val2 = list2.data if list2 else 0

        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create new node with the digit
        current.next_element = Node(digit)
        current = current.next_element

        # Move to next nodes
        list1 = list1.next_element if list1 else None
        list2 = list2.next_element if list2 else None

    return dummy_head.next_element

# 1. Define the input Python lists
l1_list = [2, 4, 3]  # Represents the number 342
l2_list = [5, 6, 4]  # Represents the number 465

# 2. Convert the Python lists into linked lists
l1_node = create_linked_list(l1_list)
l2_node = create_linked_list(l2_list)

# 3. Call the addition function with the linked list nodes
out = addition(l1_node, l2_node)

# 4. Print the result (which is also a linked list)
# Expected output represents 342 + 465 = 807
print("List 1:", end=" ")
print_linked_list(l1_node)

print("List 2:", end=" ")
print_linked_list(l2_node)

print("Result:", end=" ")
print_linked_list(out)
