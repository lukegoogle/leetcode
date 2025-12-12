class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    def reverse_linked_list(start, end):
        prev = end
        curr = start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    while True:
        k_ahead = current
        for _ in range(k):
            k_ahead = k_ahead.next
            if not k_ahead:
                return dummy.next
        
        start = current.next
        end = k_ahead.next
        
        current.next = reverse_linked_list(start, end)
        start.next = end
        current = start