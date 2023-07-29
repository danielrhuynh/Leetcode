class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, len(p)-1
        curr = Counter(s[l:r+1])
        res= []
        target = Counter(p)
        
        while r < len(s):
            # Check for res
            if curr == target:
                res.append(l)
            
            # Remove l from window
            if s[l] in curr:
                if curr[s[l]] > 1:
                    curr[s[l]] -= 1
                else:
                    curr.pop(s[l])
            
            # Slide window
            r += 1
            l += 1
            
            # Handle edge case (last iteration)
            if r >= len(s):
                break
            
            # Add r to window
            if s[r] in target:
                if s[r] not in curr:
                    curr[s[r]] = 1
                else:
                    curr[s[r]] += 1
        return res