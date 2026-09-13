class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)

        for num in nums:
            countMap[num] += 1
        
        nums.sort(key=lambda x:countMap[x], reverse=True)

        result = []
        seen = set()

        for num in nums:
            if num not in seen:
                result.append(num)
                seen.add(num)
            if len(result) == k:
                break

        
        return result


