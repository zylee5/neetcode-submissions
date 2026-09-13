class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)

        min_heap = []
        for num, freq in countMap.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])
        
        return result

