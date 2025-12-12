class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    
    for _ in range(n):
        fast = fast.next
        
    while fast.next:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    
    return dummy.next

# Example Output
l1 = create_list([1, 2, 3, 4, 5])
result = removeNthFromEnd(l1, 2)
print("--- LeetCode 19 ---")
print(f"Output for [1, 2, 3, 4, 5], n=2: {print_list(result)}")