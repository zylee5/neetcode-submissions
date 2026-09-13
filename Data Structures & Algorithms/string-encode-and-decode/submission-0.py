class Solution:

    # before '@' is sizes
    # ',' between each size

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string))
            result += ","
        result += "@"

        for string in strs:
            result += string
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        sizes = []
        i = 0
        
        while s[i] != '@':
            size = ""
            while s[i] != ',':
                size += s[i]
                i += 1
            sizes.append(int(size))
            i += 1
        i += 1

        for size in sizes:
            result.append(s[i:i + size])
            i += size
        
        return result



