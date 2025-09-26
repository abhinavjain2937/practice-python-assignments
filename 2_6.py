class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Helper 1: Reverses a linked list
def reverse_list(head: Node | None) -> Node | None:
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

# Helper 2: Prints a linked list
def print_list(head: Node | None):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print(" -> NULL")

# Main function to add the two numbers
def add_two_numbers(l1: Node | None, l2: Node | None) -> Node | None:
    # Step 1: Reverse both input lists
    r_l1 = reverse_list(l1)
    r_l2 = reverse_list(l2)
    
    carry = 0
    dummy_head = Node() # A placeholder to simplify creating the new list
    current_result = dummy_head

    # Step 2: Sum the reversed lists
    while r_l1 or r_l2 or carry:
        val1 = r_l1.data if r_l1 else 0
        val2 = r_l2.data if r_l2 else 0
        
        total_sum = val1 + val2 + carry
        
        digit = total_sum % 10
        carry = total_sum // 10
        
        # Create a new node for the result list
        current_result.next = Node(digit)
        current_result = current_result.next
        
        # Move to the next nodes in the input lists
        if r_l1: r_l1 = r_l1.next
        if r_l2: r_l2 = r_l2.next

    # Step 3: Reverse the resultant list
    result_head = reverse_list(dummy_head.next)
    
    return result_head

# --- Example Usage ---
# List1: 5->6->3 (563)
list1 = Node(5, Node(6, Node(3)))
# List2: 8->4->2 (842)
list2 = Node(8, Node(4, Node(2)))

print("List 1:")
print_list(list1)
print("List 2:")
print_list(list2)

result = add_two_numbers(list1, list2)

print("\nResultant List (563 + 842 = 1405):")
print_list(result)