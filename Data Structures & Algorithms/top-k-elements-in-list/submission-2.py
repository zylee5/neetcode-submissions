class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        unique_nums = list(counter.keys())
        unique_nums.sort(key=lambda x:counter[x], reverse=True)
        return unique_nums[:k]