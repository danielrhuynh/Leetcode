class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # exit early condition
        if len(s) != len(t):
            return False
        
        # Same length so maybe anagram
        letterMap = {}
        
        for letter in s:
            if letter not in letterMap:
                letterMap[letter] = 1
            else:
                letterMap[letter] += 1
        for letter in t:
            if letter not in letterMap or letterMap[letter] == 0:
                return False
            letterMap[letter] -= 1
        return True
            