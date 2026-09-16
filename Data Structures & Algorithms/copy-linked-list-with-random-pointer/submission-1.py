"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        oldToCopy = {}

        # Copy nodes and record hash map
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        # Link copied nodes
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy.get(curr.next)
            copy.random = oldToCopy.get(curr.random)
            curr = curr.next
        
        return oldToCopy.get(head)