class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        res = 0
        l = nums.index(1)
        while l != 0:
            nums[l], nums[l-1] = nums[l-1], nums[l]
            l -= 1
            res += 1
        r = nums.index(len(nums))
        while r != len(nums)-1:
            nums[r], nums[r+1] = nums[r+1], nums[r]
            r += 1
            res += 1
        return res
        