class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranMap = {')':'(', ']':'[','}':'{'}
        
        for char in s:
            if char in paranMap:
                if stack and paranMap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False