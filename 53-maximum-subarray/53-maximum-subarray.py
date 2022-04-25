class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        local_max = 0
        
        for n in nums:
            if local_max < 0:
                local_max = 0
            local_max += n
            max_sub = max(max_sub, local_max)
        return max_sub