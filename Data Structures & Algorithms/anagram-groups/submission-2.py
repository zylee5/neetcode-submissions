class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for string in strs:
            freqList = [0] * 26

            for char in string:
                freqList[ord(char) - ord('a')] += 1
            
            anagramMap[tuple(freqList)].append(string)
        
        return list(anagramMap.values())
