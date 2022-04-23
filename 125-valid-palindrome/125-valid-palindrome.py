class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredS = "".join(c for c in s if c.isalnum()).lower()
        
        l, r = 0, len(filteredS)-1
        while l < r:
            if filteredS[l] != filteredS[r]:
                return False
            l += 1
            r -= 1
        print (filteredS)
        return True