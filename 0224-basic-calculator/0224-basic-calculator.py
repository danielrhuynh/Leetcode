class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        curr = 0
        sign = 1
        stack = []
        for i in range(len(s)):
            # Checking for a digit
            if s[i].isdigit():
                # moves curr one decimal place to the left and add new digit
                curr = curr*10+int(s[i])
            # Here we finished proccessing the previous thing
            elif s[i] == '+' or s[i] == '-':
                res += sign*curr
                # Now reset variables for next iteration
                sign = 1 if s[i] == '+' else -1
                curr = 0
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                # Now we start a new iteration
                sign = 1
                res = 0
            elif s[i] == ')':
                res += sign*curr
                sign = stack.pop()
                sum = stack.pop()
                res *= sign
                res += sum
                
                # Finished processing, next iteration
                curr = 0
        # Handling remaining integer at end of expression
        return res + sign*curr
            
            