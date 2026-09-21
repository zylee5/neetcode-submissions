class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first, second = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            # do nothing if equal (second > first is not possible)
            if first > second:
                diff = first - second
                heapq.heappush(maxHeap, -diff)
        
        return -maxHeap[0] if maxHeap else 0