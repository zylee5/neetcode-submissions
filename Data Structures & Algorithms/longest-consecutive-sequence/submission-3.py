class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0

        for num in unique:
            if (num - 1) not in unique:
                # start of a sequence
                length = 1
                while (num + length) in unique:
                    length += 1
                longest = max(longest, length)
        
        return longest