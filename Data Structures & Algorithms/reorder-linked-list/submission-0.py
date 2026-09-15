# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None # Separate two lists

        # Reverse second list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge
        first, second = head, prev
        while second: # Second list is always shorter or equal in length
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
