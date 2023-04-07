class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group using hashmap of res values by ascii key (too expensive)
        # Group using sorted string so anagrams have a common key
        res = []
        trans = {} # Translations dictionary
        resCount = 0
        
        for string in strs:
            key = "".join(sorted(string))
            if key not in trans:
                res.append([])
                trans[key] = resCount
                resCount += 1
            res[trans[key]].append(string)
        return res
            
            
        
        