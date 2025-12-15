class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        for _ in range(n + 1):
            if not fast:
                return head
            fast = fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next
