from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
                current = list1
                list1 = list1.next
        else:
                current = list2
                list2 = list2.next
        
        res = current
        if list1 is None:
                current.next = list2
        if list2 is None:
                current.next = list1
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            if list1 is None:
                current.next = list2
                pass
            if list2 is None:
                current.next = list1
                pass
        
        return res
            



def list_to_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_solution():
    test_cases = [
        ([1], [2], [1, 2]),
        ([1, 2, 4], [1, 3, 5], [1, 1, 2, 3, 4, 5]),
        ([], [1, 2], [1, 2]),
        ([], [], [])
    ]
    
    solution = Solution()
    
    for i, (list1, list2, expected_output) in enumerate(test_cases):
        head1 = list_to_linked_list(list1)
        head2 = list_to_linked_list(list2)
        merged_head = solution.mergeTwoLists(head1, head2)
        output_list = linked_list_to_list(merged_head)
        print(f"Merged List: {output_list}")
        print(f"Test case {i + 1}: {'Passed' if output_list == expected_output else 'Failed'}")
        
test_solution()
