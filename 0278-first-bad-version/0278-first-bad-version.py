# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Binary search Q
        low, high = 0, n
        while low < high:
            mid = (high+low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low # This converges on the first bad version
        