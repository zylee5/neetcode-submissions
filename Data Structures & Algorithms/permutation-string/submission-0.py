class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freqMap1 = defaultdict(int)
        for s in s1:
            freqMap1[s] += 1

        left = 0
        right = len(s1) - 1

        while right < len(s2):
            freqMap2 = defaultdict(int)
            for idx in range(left, right + 1):
                freqMap2[s2[idx]] += 1
            
            match = 0
            for idx in range(left, right + 1):
                if freqMap1[s2[idx]] == freqMap2[s2[idx]]:
                    match += 1
            
            if match == right - left + 1:
                return True
            
            left += 1
            right += 1
        
        return False
