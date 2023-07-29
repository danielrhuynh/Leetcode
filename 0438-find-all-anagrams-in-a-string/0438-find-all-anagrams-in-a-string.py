class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, len(p)-1
        curr = Counter(s[l:r+1])
        res= []
        
        
        target = Counter(p)
        
        while r < len(s):
            if curr == target:
                res.append(l)
                
            if s[l] in curr:
                if curr[s[l]] > 1:
                    curr[s[l]] -= 1
                else:
                    curr.pop(s[l])
            r += 1
            l += 1
            if r >= len(s):
                break
            if s[r] in target:
                if s[r] not in curr:
                    curr[s[r]] = 1
                else:
                    curr[s[r]] += 1
        return res