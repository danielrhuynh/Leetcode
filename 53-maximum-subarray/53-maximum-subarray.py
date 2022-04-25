class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        local_max = 0
        
        for i in range(len(nums)):
            local_max = max(nums[i], local_max + nums[i])
            max_sub = max(local_max, max_sub)
        return max_sub