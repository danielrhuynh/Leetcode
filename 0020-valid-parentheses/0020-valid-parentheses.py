class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        parenMap = {')': '(', ']':'[', '}':'{'}
        stack = []
        
        for char in s:
            if char in parenMap.keys():
                if not stack:
                    return False
                if stack[-1] == parenMap[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True
        
        