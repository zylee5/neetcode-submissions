# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0 # Num of nodes
        curr = head
        while curr:
            N += 1
            curr = curr.next
        
        removeIdx = N - n
        dummy = ListNode(0, head)
        curr = dummy

        # Move to the node before the one to remove
        for i in range(removeIdx):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next