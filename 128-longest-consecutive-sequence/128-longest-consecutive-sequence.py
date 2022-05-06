class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = {}
        nums.sort()
        ctr, maxCtr = 1,1
        last = nums[0]
        
        for n in nums:
            seen[n] = 1
            if n-1 in seen and seen[n-1] < 2:
                ctr += 1
                seen[n-1] += 1
            elif n == last:
                continue
            else:
                ctr = 1
            maxCtr = max(maxCtr, ctr)
            last = n
        return maxCtr