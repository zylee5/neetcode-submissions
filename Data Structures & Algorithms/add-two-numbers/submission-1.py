# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = res = ListNode(0)
        carry = 0

        while l1 or l2:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0

            total = first + second + carry
            if total >= 10:
                carry = 1
                res.next = ListNode(total - 10)
            else:
                carry = 0
                res.next = ListNode(total)
            
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            res.next = ListNode(carry)
        
        return dummy.next
