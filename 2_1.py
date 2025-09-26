

# Definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle_node(head: ListNode) -> ListNode:
    """Finds the middle of a linked list using the slow and fast pointer method."""
    # using two pointers to get the two resultas at a same time
    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    
    return slow_ptr



list1 = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
middle1 = find_middle_node(list1)
print(f"Test Case 1 : The middle element is {middle1.val}")

