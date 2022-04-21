class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        trans = {}
        
        for s in strs:
            key = "".join(sorted(s))
            if key not in trans:
                res.append([])
                trans[key] = res.index([])
            res[trans[key]].append(s)
        return res
                