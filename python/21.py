class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        
    current.next = list1 if list1 else list2
    
    return dummy.next

# Example Output
l1 = create_list([1, 2, 4])
l2 = create_list([1, 3, 4])
result = mergeTwoLists(l1, l2)
print("--- LeetCode 21 ---")
print(f"Output for [1, 2, 4] and [1, 3, 4]: {print_list(result)}")