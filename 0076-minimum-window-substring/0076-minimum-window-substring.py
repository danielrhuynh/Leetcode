class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = Counter(t), {}
        
        have, need = 0, len(countT)
        
        res, resLen = [-1, -1], float("infinity")
        l = 0
        
        # Iterate over s
        for r in range(len(s)):
            c = s[r]
            # Add c to curr
            window[c] = 1 + window.get(c, 0)
            
            # If c is in target and values are exactly equal
            if c in countT and window[c] == countT[c]:
                have += 1
            # If our condiiton is met
            while have == need:
                # Update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from left of window
                window[s[l]] -= 1
                # if we no longer satisfy a condition reduce have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # Move window
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""