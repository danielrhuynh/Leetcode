class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = {}
        max_count = 0
        
        while right < len(s):
            if s[right] in seen:
                if len(seen) > max_count:
                    max_count = len(seen)
                seen.pop(s[left])
                left += 1
            else:
                seen[s[right]] = 1
                right +=1
        return max(max_count, len(seen))