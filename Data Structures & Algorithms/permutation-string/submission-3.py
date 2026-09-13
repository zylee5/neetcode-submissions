class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        if s1Count == s2Count:
            return True
        
        for i in range(len(s1), len(s2)):
            # Char that is removed from the left
            s2Count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # Char that is added to the right
            s2Count[ord(s2[i]) - ord('a')] += 1
            if s1Count == s2Count:
                return True
                        
        return False
