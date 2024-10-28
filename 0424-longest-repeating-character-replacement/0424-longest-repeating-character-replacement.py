class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        L = 0
        res = 0

        for R in range(len(s)):
            if s[R] in seen:
                seen[s[R]] += 1
            else:
                seen[s[R]] = 1

            curr = R - L + 1 - max(seen.values())

            if curr <= k:
                res = max(res, R - L + 1)
            else:
                seen[s[L]] -= 1
                L += 1
        return res