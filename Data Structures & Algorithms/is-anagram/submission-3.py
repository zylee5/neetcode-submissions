class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map_s = {}
        hash_map_t = {}
        for char in s:
            if not hash_map_s.get(char):
                hash_map_s[char] = 1
            else:
                hash_map_s[char] += 1
        
        for char in t:
            if not hash_map_t.get(char):
                hash_map_t[char] = 1
            else:
                hash_map_t[char] += 1
        
        for char in s:
            if hash_map_s.get(char) != hash_map_t.get(char):
                return False
        
        return True



        