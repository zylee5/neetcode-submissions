class Solution:

    # length@string

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + '@' + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            size = int(s[i:j])
            j += 1
            i = j
            result.append(s[i:i + size])
            i += size
        
        return result



