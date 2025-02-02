class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev
            

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
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], [])
    ]
    
    solution = Solution()
    
    for i, (input_list, expected_output) in enumerate(test_cases):
        head = list_to_linked_list(input_list)
        reversed_head = solution.reverseList(head)
        output_list = linked_list_to_list(reversed_head)
        print(f"Test case {i + 1}: {'Passed' if output_list == expected_output else 'Failed'}")
        
test_solution()
