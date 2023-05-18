class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Would be really easy if you could use the division operator
        # Use a prefix postfix approach
        res = [1] * len(nums)
        product = 1
        # Getting prefix array using nums
        for i in range(len(nums)):
            res[i] *= product
            product *= nums[i]
        product = 1
        # Second pass applying postfix
        for i in range(len(nums)-1, -1, -1):
            res[i] *= product
            product *= nums[i]
        return res
            
        
            
        