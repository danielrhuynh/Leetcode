class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterMap = {}
        
        for string in strs:
            key = ''.join(sorted(string))
            if key in letterMap:
                letterMap[key].append(string)
            else:
                letterMap[key] = [string]
        
        return [letterMap[key] for key in letterMap]
            