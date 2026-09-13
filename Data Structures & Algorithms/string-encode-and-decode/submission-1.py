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
            sizeStr = ""
            while s[i] != '@':
                sizeStr += s[i]
                i += 1
            size = int(sizeStr)
            i += 1
            result.append(s[i:i + size])
            i += size
        
        return result



