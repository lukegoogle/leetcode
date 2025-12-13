# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            sum_val = val1 + val2 + carry
            
            carry = sum_val // 10
            new_digit = sum_val % 10
            
            current.next = ListNode(new_digit)
            current = current.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy_head.next
    
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(node):
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result

solver = Solution()

# Test Case 1: 342 + 465 = 807
arr1_1 = [2, 4, 3]
arr1_2 = [5, 6, 4]
l1_1 = create_linked_list(arr1_1)
l1_2 = create_linked_list(arr1_2)
result1 = solver.addTwoNumbers(l1_1, l1_2)

print(f"Input L1 (Reversed): {arr1_1}")
print(f"Input L2 (Reversed): {arr1_2}")
print(f"Output (Reversed): {print_linked_list(result1)}")

# Test Case 2: 99 + 9999 = 10098
arr2_1 = [9, 9]
arr2_2 = [9, 9, 9, 9]
l2_1 = create_linked_list(arr2_1)
l2_2 = create_linked_list(arr2_2)
result2 = solver.addTwoNumbers(l2_1, l2_2)

print(f"\nInput L1 (Reversed): {arr2_1}")
print(f"Input L2 (Reversed): {arr2_2}")
print(f"Output (Reversed): {print_linked_list(result2)}")