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
    
# --- Helper function for list creation and printing ---

def create_linked_list(arr: list[int]) -> ListNode | None:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head: ListNode | None):
    if not head:
        return "[]"
    
    nodes = []
    current = head
    while current:
        nodes.append(str(current.val))
        current = current.next
    return "[" + " -> ".join(nodes) + "]"


# --- Example Usage Code ---

sol = Solution()
print("--- Remove Nth Node From End of List Examples ---")

# Test Case 1: Standard case
arr1 = [1, 2, 3, 4, 5]
n1 = 2
head1 = create_linked_list(arr1)
result1 = sol.removeNthFromEnd(head1, n1)
# Expected: [1 -> 2 -> 3 -> 5]
print(f"Input List: {print_linked_list(create_linked_list(arr1))}, n={n1}")
print(f"Output List: {print_linked_list(result1)}")

# Test Case 2: Remove the head (n = list length)
arr2 = [1]
n2 = 1
head2 = create_linked_list(arr2)
result2 = sol.removeNthFromEnd(head2, n2)
# Expected: []
print(f"Input List: {print_linked_list(create_linked_list(arr2))}, n={n2}")
print(f"Output List: {print_linked_list(result2)}")

# Test Case 3: List with two nodes, remove the first one
arr3 = [1, 2]
n3 = 2
head3 = create_linked_list(arr3)
result3 = sol.removeNthFromEnd(head3, n3)
# Expected: [2]
print(f"Input List: {print_linked_list(create_linked_list(arr3))}, n={n3}")
print(f"Output List: {print_linked_list(result3)}")

# Test Case 4: Larger example, remove node in the middle
arr4 = [10, 20, 30, 40, 50, 60]
n4 = 3 # Removes 40
head4 = create_linked_list(arr4)
result4 = sol.removeNthFromEnd(head4, n4)
# Expected: [10 -> 20 -> 30 -> 50 -> 60]
print(f"Input List: {print_linked_list(create_linked_list(arr4))}, n={n4}")
print(f"Output List: {print_linked_list(result4)}")