class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) <= 0:
            return 0
        
        left, right = 0, 0
        unique = set()
        longest = 0

        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                longest = max(longest, right - left + 1)
                right += 1
            else:
                while left < right and s[right] in unique:
                    unique.remove(s[left])
                    left += 1
        
        return longest
