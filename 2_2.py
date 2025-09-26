class Node:
    count = 0
    def __init__(self,data,next = None) -> None:
        self.data = data 
        self.next = next
        Node.count+=1

    
def mid_deletion(listl:Node):
    current = listl
    mid = (listl.count//2)
    for _ in range(mid - 1):     # Stop at node before middle
        current = current.next
        before_mid = current.next

    # Remove middle node safely
    if current.next:

        current.next = current.next.next
        data = current
        cnt = listl.count-1
    return data,cnt,before_mid

# def find(head:Node)->Node:
#     slow = head
#     fast = head
#     count = 0
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         count+=1
#     return slow , count

listl = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9)))))))))
# mid , num = find(listl)
# print(mid.data)
# print(num)


print(listl.count,": the count of no of elements in the list after deletion")

data_add , cnt,befor_mid = mid_deletion(listl)

print(f"the mid before deletion: {befor_mid.data} ")




print(cnt,": the count of no of elements in the list after deletion")
print(f" the mid after deletion : {data_add.data}")
print("____",data_add.data)

