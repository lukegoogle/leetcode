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
print("--- Reverse Nodes in k-Group Examples ---")

# Test Case 1: Standard case (k=2)
arr1 = [1, 2, 3, 4, 5]
k1 = 2
head1 = create_linked_list(arr1)
result1 = sol.reverseKGroup(head1, k1)
# Expected: [2 -> 1 -> 4 -> 3 -> 5]
print(f"Input List: {print_linked_list(create_linked_list(arr1))}, k={k1}")
print(f"Output List: {print_linked_list(result1)}")

# Test Case 2: Standard case (k=3)
arr2 = [1, 2, 3, 4, 5]
k2 = 3
head2 = create_linked_list(arr2)
result2 = sol.reverseKGroup(head2, k2)
# Expected: [3 -> 2 -> 1 -> 4 -> 5] (The last two nodes are not reversed)
print(f"Input List: {print_linked_list(create_linked_list(arr2))}, k={k2}")
print(f"Output List: {print_linked_list(result2)}")

# Test Case 3: Empty list
arr3 = []
k3 = 2
head3 = create_linked_list(arr3)
result3 = sol.reverseKGroup(head3, k3)
# Expected: []
print(f"Input List: {print_linked_list(create_linked_list(arr3))}, k={k3}")
print(f"Output List: {print_linked_list(result3)}")

# Test Case 4: k is greater than list length
arr4 = [1, 2]
k4 = 3
head4 = create_linked_list(arr4)
result4 = sol.reverseKGroup(head4, k4)
# Expected: [1 -> 2] (No reversal occurs)
print(f"Input List: {print_linked_list(create_linked_list(arr4))}, k={k4}")
print(f"Output List: {print_linked_list(result4)}")