class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        L = R = 0
        res = 0
        while R < len(s):
            if s[R] not in curr:
                curr.add(s[R])
                R += 1
            else:
                res = max(res, len(curr))
                curr.remove(s[L])
                L += 1
        res = max(res, len(curr))
        return res
            
            
