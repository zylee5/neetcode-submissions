class Node:
    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # self.left.next -> least recently used
        # self.right.prev -> most recently used
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left

    # Remove node from the list - O(1) time
    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert node before nodeBefore - O(1) time
    def insertBefore(self, node, nodeBefore) -> None:
        prev = nodeBefore.prev
        prev.next = node
        node.prev, node.next = prev, nodeBefore
        nodeBefore.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertBefore(node, self.right)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insertBefore(node, self.right)
            return
            
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insertBefore(newNode, self.right)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
