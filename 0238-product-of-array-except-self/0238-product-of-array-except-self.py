class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Seems like a permutations questions
        # O(n) only run through the array once
        # Prefix and postfix
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
            
            
        
            
        