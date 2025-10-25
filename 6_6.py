# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    Given the head of a sorted linked list, deletes all duplicates.
    """
    # Start traversal from the head of the list
    current = head
    
    # Traverse the list until the second to last node
    while current and current.next:
        # If the next node is a duplicate
        if current.val == current.next.val:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            # If not a duplicate, move to the next node
            current = current.next
            
    return head

# --- Helper Functions for the Example ---

def create_linked_list(items: list) -> ListNode:
    """Converts a Python list to a linked list."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

def print_list(head: ListNode) -> list:
    """Converts a linked list back to a Python list for printing."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# --- Example Implementation ---

# Example 1: Input: head = [1,1,2]
input_data_1 = [1, 1, 2]
head_1 = create_linked_list(input_data_1)
result_head_1 = deleteDuplicates(head_1)
output_1 = print_list(result_head_1)

print(f"Input: {input_data_1}")
print(f"Output: {output_1}\n") # Expected: [1, 2]

# Example 2: Input: head = [1,1,2,3,3]
input_data_2 = [1, 1, 2, 3, 3]
head_2 = create_linked_list(input_data_2)
result_head_2 = deleteDuplicates(head_2)
output_2 = print_list(result_head_2)

print(f"Input: {input_data_2}")
print(f"Output: {output_2}") # Expected: [1, 2, 3]