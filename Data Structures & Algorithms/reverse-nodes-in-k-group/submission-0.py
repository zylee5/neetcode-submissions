# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(0, head)
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            cur = groupPrev.next
            prev = groupNext # reversed group's tail should point to groupNext
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = groupPrev.next # now last node in the reversed group
            groupPrev.next = kth # point to the new first node in the reversed group
            groupPrev = temp
        return dummy.next 
    
    def getKth(self, node, k):
        cur = node
        while k > 0 and cur:
            cur = cur.next
            k -= 1
        return cur
