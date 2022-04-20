class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        s = s.split(' ')
        for i in range(len(s)):
            word = s[i]
            for j in range(len(word)-1, -1, -1):
                res += word[j]
            if i < len(s)-1:
                res += ' '
        return res