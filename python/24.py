class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        
        current.next = second
        first.next = second.next
        second.next = first
        
        current = current.next.next
        
    return dummy.next

# Example Output
l1 = create_list([1, 2, 3, 4])
result = swapPairs(l1)
print("--- LeetCode 24 ---")
print(f"Output for [1, 2, 3, 4]: {print_list(result)}")