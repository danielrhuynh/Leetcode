class Solution:
    def myAtoi(self, s: str) -> int:
        # Strip whitespace
        s = s.lstrip()
        
        # Check for string still existing
        if not s:
            return 0
        
        # Checking for any leading signs
        i = 0
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        
        parsed = 0
        
        # Parsing string
        while i < len(s):
            curr = s[i]
            if not curr.isdigit():
                break
            # else we found a valid char
            else:
                # How we parse strings as ints (moving 10's places (l -> r))
                parsed = parsed * 10 + int(curr)
            i += 1
        
        # Checking to see if parsed is in range
        parsed *= sign
        if parsed > 2**31 - 1:
            return 2**31-1
        elif parsed <= -2**31:
            return -2**31
        return parsed