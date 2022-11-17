class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''
        tCount = Counter(t)
        window = {}
        
        have, need = 0, len(tCount)
        res, resLen = [-1, -1], float('infinity')
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) +1
            
            if char in tCount and window[char] == tCount[char]:
                have += 1
            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l, r]
                    
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ''
                    