class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        unique = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            longest = max(longest, right - left + 1)

        return longest