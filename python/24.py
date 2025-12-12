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
l1 = create_list([1, 2, 3, 4])
result1 = swapPairs(l1)
print(f"Output for [1, 2, 3, 4]: {print_list(result1)}")

l2 = create_list([])
result2 = swapPairs(l2)
print(f"Output for []: {print_list(result2)}")

l3 = create_list([1])
result3 = swapPairs(l3)
print(f"Output for [1]: {print_list(result3)}")