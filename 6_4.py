# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

# --- Core Logic ---

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    """Helper function to merge two sorted linked lists."""
    dummy_head = ListNode()
    tail = dummy_head
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
        
    tail.next = l1 if l1 else l2
    return dummy_head.next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    """
    Merges k sorted linked lists using a divide and conquer strategy.
    """
    if not lists:
        return None
        
    amount = len(lists)
    interval = 1
    
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
        
    return lists[0] if amount > 0 else None


# --- Running the Example ---

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
input_lists_data = [[1, 4, 5], [1, 3, 4], [2, 6]]

# 1. Convert the python lists into actual ListNode objects
linked_lists = [create_linked_list(l) for l in input_lists_data]

# 2. Run the mergeKLists function
merged_head = mergeKLists(linked_lists)

# 3. Print the output in the desired format
output_list = print_list(merged_head)

print(f"Input: {input_lists_data}")
print(f"Output: {output_list}")

print("\nExplanation: The linked-lists are:")
print("[\n  1->4->5,\n  1->3->4,\n  2->6\n]")
print("merging them into one sorted list:")
final_str = "->".join(map(str, output_list))
print(final_str)