---
hide:
  - navigation
  - toc
---

# Pyodide

```pyodide height="20"

# Leetcode 2 Verbose

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_digit = total_sum % 10
            print(f"(new_digit) {new_digit}: (total_sum) {total_sum} = (Val1) {val1} + (Val2) {val2} + (carry) {carry}")

            current.next = ListNode(new_digit)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next
    
# Helper function to convert a list of digits to a linked list (in reverse order)
def create_linked_list(digits):
    dummy_head = ListNode(0)
    current = dummy_head
    for digit in digits:
        current.next = ListNode(digit)
        current = current.next
    return dummy_head.next

# Helper function to convert a linked list to a list of digits
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Example 1: (2 -> 4 -> 3) + (5 -> 6 -> 4) -> (7 -> 0 -> 8)
l1_ex1 = create_linked_list([2, 4, 3])
l2_ex1 = create_linked_list([5, 6, 4])
print(linked_list_to_list(Solution().addTwoNumbers(l1_ex1, l2_ex1)), "\n")

# Example 2: (0) + (0) -> (0)
l1_ex2 = create_linked_list([0])
l2_ex2 = create_linked_list([0])
print(linked_list_to_list(Solution().addTwoNumbers(l1_ex2, l2_ex2)), "\n")

# Example 3: (9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9) + (9 -> 9 -> 9 -> 9) -> (8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1)
l1_ex3 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2_ex3 = create_linked_list([9, 9, 9, 9])
print(linked_list_to_list(Solution().addTwoNumbers(l1_ex3, l2_ex3)))

```