class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        l = r = 0
        res = 0
        
        while r < len(s):
            if s[r] in curr:
                res = max(res, len(curr))
                curr.remove(s[l])
                l += 1
            else:
                curr.add(s[r])
                r += 1
        return max(res, len(curr))
            