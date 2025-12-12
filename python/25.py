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

# Helper functions for example output
def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example Output
l1 = create_list([1, 2, 3, 4, 5])
result1 = reverseKGroup(l1, 2)
print(f"Output for [1, 2, 3, 4, 5], k=2: {print_list(result1)}")

l2 = create_list([1, 2, 3, 4, 5])
result2 = reverseKGroup(l2, 3)
print(f"Output for [1, 2, 3, 4, 5], k=3: {print_list(result2)}")