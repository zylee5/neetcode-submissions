class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        freqList = [[] for i in range(len(nums) + 1)]

        for num, freq in countMap.items():
            freqList[freq].append(num)
        
        result = []
        for i in range(len(nums), -1, -1):
            for num in freqList[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
