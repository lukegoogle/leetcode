import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
                
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
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
print("--- Merge k Sorted Lists Examples ---")

# Test Case 1: Standard k=3 lists
arr1 = [1, 4, 5]
arr2 = [1, 3, 4]
arr3 = [2, 6]
lists1 = [create_linked_list(arr1), create_linked_list(arr2), create_linked_list(arr3)]
result1 = sol.mergeKLists(lists1)
# Expected: [1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6]
print(f"Input Lists: {[[1, 4, 5], [1, 3, 4], [2, 6]]}")
print(f"Output List: {print_linked_list(result1)}")

# Test Case 2: Empty input list
lists2 = []
result2 = sol.mergeKLists(lists2)
# Expected: []
print(f"Input Lists: {[]}")
print(f"Output List: {print_linked_list(result2)}")

# Test Case 3: List containing empty lists
arr4 = []
arr5 = [1, 5]
arr6 = [2, 4]
lists3 = [create_linked_list(arr4), create_linked_list(arr5), create_linked_list(arr6)]
result3 = sol.mergeKLists(lists3)
# Expected: [1 -> 2 -> 4 -> 5]
print(f"Input Lists: {[[2, 4], [1, 5], []]}")
print(f"Output List: {print_linked_list(result3)}")

# Test Case 4: Single list in the input
lists4 = [create_linked_list([10, 20, 30])]
result4 = sol.mergeKLists(lists4)
# Expected: [10 -> 20 -> 30]
print(f"Input Lists: {[[10, 20, 30]]}")
print(f"Output List: {print_linked_list(result4)}")