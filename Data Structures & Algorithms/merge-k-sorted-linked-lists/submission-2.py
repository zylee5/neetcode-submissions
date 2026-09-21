# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        minHeap = []

        # O(klogk)
        for lst in lists:
            if lst:
                heapq.heappush(minHeap, NodeWrapper(lst))
        
        # O(nlogk), n>=k
        dummy = cur = ListNode()
        while minHeap:
            minNode = heapq.heappop(minHeap)
            cur.next = minNode.node
            if minNode.node.next:
                heapq.heappush(minHeap, NodeWrapper(minNode.node.next))
            cur = cur.next
        
        return dummy.next
