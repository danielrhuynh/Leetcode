class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        i = 1
        l, r = 0, 1
        ctr, maxCtr = 1,1
        
        while r < len(nums):
            if nums[r] == nums[r-1]:
                r += 1
                continue
            elif  nums[r]-i == nums[l]:
                ctr += 1
                i += 1
                r += 1
            else:
                i = 1
                l = r
                r += 1
                ctr = 1
            maxCtr = max(maxCtr, ctr)
        return maxCtr
                
                
                