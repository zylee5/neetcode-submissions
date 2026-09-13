class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        countT = defaultdict(int)
        for char in t:
            countT[char] += 1
        
        resIndices = [-1, -1]
        resLen = float('inf')

        windowCount = defaultdict(int)
        matches = 0
        need = len(countT)

        left = 0
        for right in range(len(s)):
            charRight = s[right]
            windowCount[charRight] += 1

            if charRight in countT and windowCount[charRight] == countT[charRight]:
                matches += 1
            
            while matches == need:
                if (right - left + 1) < resLen:
                    resIndices = [left, right]
                    resLen = right - left + 1
                
                charLeft = s[left]
                windowCount[charLeft] -= 1
                if charLeft in countT and windowCount[charLeft] < countT[charLeft]:
                    matches -= 1
                left += 1
        
        left, right = resIndices
        return s[left:right + 1] if resLen != float('inf') else ""
        