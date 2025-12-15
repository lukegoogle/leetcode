class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        
        while True:
            kth = head
            for _ in range(k - 1):
                if not kth:
                    break
                kth = kth.next
            
            if not kth:
                break
                
            next_group_head = kth.next
            
            curr, prev = head, next_group_head
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            prev_group_tail.next = prev
            prev_group_tail = head
            head = next_group_head
            
        return dummy.next