class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCounts = Counter(s)
        res = 0
        oddFound = False
        
        for i in charCounts.values():
            if i % 2 == 0:
                res += i
            else:
                if oddFound:
                    res += i-1
                else:
                    res += i
                    oddFound = True
        return res