class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # base case: only one permutation
        if len(nums) <= 1:
            return [nums.copy()]
        
        # for every value in nums
        for i in range(len(nums)):
            # remove first value
            n = nums.pop(0)
            # find permutations of remainders
            perms = self.permute(nums)
            
            # add the removed value to every permutation
            for perm in perms:
                perm.append(n)
                res.append(perm)
            # add removed value back to nums
            nums.append(n)
        return res