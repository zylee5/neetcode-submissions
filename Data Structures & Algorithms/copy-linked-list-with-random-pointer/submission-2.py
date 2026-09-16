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
        oldToCopy = collections.defaultdict(lambda: Node(0)) # Placeholder nodes
        oldToCopy[None] = None # For null next/random pointers

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.val = curr.val # Fill in the placeholder node
            # Do not use .get because it would return None instead of creating a placeholder
            copy.next = oldToCopy[curr.next] 
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]