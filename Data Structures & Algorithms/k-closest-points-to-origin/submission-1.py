class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            # sqrt is not required
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(maxHeap, (-dist, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            point = heapq.heappop(maxHeap)[1]
            res.append(point)
        return res