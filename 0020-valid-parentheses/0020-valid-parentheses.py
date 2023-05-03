class Solution:
    def isValid(self, s: str) -> bool:
        # Exit early
        if len(s) <= 1:
            return False
        # Use a stack
        # Need to recognize close parens to open parens:
        toCloseMap = {')':'(', ']':'[', '}':'{'}
        parenStack = []
        for paren in s:
            if paren not in toCloseMap:
                parenStack.append(paren)
            else:
                if parenStack and parenStack[-1] == toCloseMap[paren]:
                    parenStack.pop(-1)
                else:
                    return False
        return not len(parenStack)