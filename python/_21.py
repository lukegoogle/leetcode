class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        current.next = list1 if list1 else list2
        
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
print("--- Merge Two Sorted Lists Examples ---")

# Test Case 1: Standard merge
arr1 = [1, 2, 4]
arr2 = [1, 3, 4]
list1 = create_linked_list(arr1)
list2 = create_linked_list(arr2)
result1 = sol.mergeTwoLists(list1, list2)
# Expected: [1 -> 1 -> 2 -> 3 -> 4 -> 4]
print(f"List 1: {print_linked_list(create_linked_list(arr1))}")
print(f"List 2: {print_linked_list(create_linked_list(arr2))}")
print(f"Output: {print_linked_list(result1)}")

# Test Case 2: One empty list
arr3 = []
arr4 = [0]
list3 = create_linked_list(arr3)
list4 = create_linked_list(arr4)
result2 = sol.mergeTwoLists(list3, list4)
# Expected: [0]
print(f"List 1: {print_linked_list(create_linked_list(arr3))}")
print(f"List 2: {print_linked_list(create_linked_list(arr4))}")
print(f"Output: {print_linked_list(result2)}")

# Test Case 3: Both empty lists
arr5 = []
arr6 = []
list5 = create_linked_list(arr5)
list6 = create_linked_list(arr6)
result3 = sol.mergeTwoLists(list5, list6)
# Expected: []
print(f"List 1: {print_linked_list(create_linked_list(arr5))}")
print(f"List 2: {print_linked_list(create_linked_list(arr6))}")
print(f"Output: {print_linked_list(result3)}")

# Test Case 4: One list contains all smaller elements
arr7 = [1, 2, 3]
arr8 = [4, 5, 6]
list7 = create_linked_list(arr7)
list8 = create_linked_list(arr8)
result4 = sol.mergeTwoLists(list7, list8)
# Expected: [1 -> 2 -> 3 -> 4 -> 5 -> 6]
print(f"List 1: {print_linked_list(create_linked_list(arr7))}")
print(f"List 2: {print_linked_list(create_linked_list(arr8))}")
print(f"Output: {print_linked_list(result4)}")