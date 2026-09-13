class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        result = []

        for index, string in enumerate(strs):
            sortedString = "".join(sorted(string))
            if sortedString in anagramMap:
                anagramMap[sortedString].append(string)
            else:
                anagramMap[sortedString] = [string]

        for anagrams in anagramMap.values():
            result.append(anagrams)
        
        return result
            

