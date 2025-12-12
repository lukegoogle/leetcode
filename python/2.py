class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        new_digit = total_sum % 10
        
        current.next = ListNode(new_digit)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy_head.next

# Example Output helper function
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

l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])
result = addTwoNumbers(l1, l2)
print("--- LeetCode 2 ---")
print(f"Output for [2, 4, 3] + [5, 6, 4]: {print_list(result)}")