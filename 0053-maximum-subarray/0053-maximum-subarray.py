class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Exit early case
        if len(nums) == 1:
            return nums[0]
        # More than 1 element
        globalMax = nums[0]
        localMax = 0
        ptr = 0
        
        while ptr < len(nums):
            if localMax < 0:
                localMax = 0
            localMax += nums[ptr]
            globalMax = max(globalMax, localMax)
            ptr += 1
        return globalMax
        
            