class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        historyMaxFreq = 0
        freqMap = defaultdict(int)
        longest = 0

        for right in range(len(s)):
            freqMap[s[right]] += 1
            historyMaxFreq = max(historyMaxFreq, freqMap[s[right]])

            while (right - left + 1) - historyMaxFreq > k:
                freqMap[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest