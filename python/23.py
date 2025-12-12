class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
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

def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists:
        return None
    
    amount = len(lists)
    interval = 1
    
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
        
    return lists[0] if amount > 0 else None

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
lists1 = [create_list([1, 4, 5]), create_list([1, 3, 4]), create_list([2, 6])]
result1 = mergeKLists(lists1)
print(f"Output for [[1, 4, 5], [1, 3, 4], [2, 6]]: {print_list(result1)}")

lists2 = []
result2 = mergeKLists(lists2)
print(f"Output for []: {print_list(result2)}")