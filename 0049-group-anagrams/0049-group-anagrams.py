class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            ctr = tuple(sorted(Counter(s).items()))
            if ctr in res:
                res[ctr].append(s)
            else:
                res[ctr] = [s]
        return res.values()
            
            
        
        