class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            
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
print("--- Swap Nodes in Pairs Examples ---")

# Test Case 1: Standard case (even number of nodes)
arr1 = [1, 2, 3, 4]
head1 = create_linked_list(arr1)
result1 = sol.swapPairs(head1)
# Expected: [2 -> 1 -> 4 -> 3]
print(f"Input List: {print_linked_list(create_linked_list(arr1))}")
print(f"Output List: {print_linked_list(result1)}")

# Test Case 2: Odd number of nodes (last node remains in place)
arr2 = [1, 2, 3, 4, 5]
head2 = create_linked_list(arr2)
result2 = sol.swapPairs(head2)
# Expected: [2 -> 1 -> 4 -> 3 -> 5]
print(f"Input List: {print_linked_list(create_linked_list(arr2))}")
print(f"Output List: {print_linked_list(result2)}")

# Test Case 3: Empty list
arr3 = []
head3 = create_linked_list(arr3)
result3 = sol.swapPairs(head3)
# Expected: []
print(f"Input List: {print_linked_list(create_linked_list(arr3))}")
print(f"Output List: {print_linked_list(result3)}")

# Test Case 4: Single node
arr4 = [1]
head4 = create_linked_list(arr4)
result4 = sol.swapPairs(head4)
# Expected: [1]
print(f"Input List: {print_linked_list(create_linked_list(arr4))}")
print(f"Output List: {print_linked_list(result4)}")