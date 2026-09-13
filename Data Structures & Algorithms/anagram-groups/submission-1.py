class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for string in strs:
            sortedString = "".join(sorted(string))
            anagramMap[sortedString].append(string)
        
        return list(anagramMap.values())