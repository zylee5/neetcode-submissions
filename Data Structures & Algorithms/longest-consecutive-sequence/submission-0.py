class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        result = 0

        for num in nums:
            val = num
            streak = 0
            while val in unique:
                streak += 1
                val += 1
            result = max(result, streak)

        return result