class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        trans = {")":"(", "]":"[","}":"{"}
        
        for char in s:
            if len(stack) > 0 and char in trans and stack[-1] == trans[char]:
                stack.pop()
            else:
                stack.append(char)
        if not stack:
            return True
        return False