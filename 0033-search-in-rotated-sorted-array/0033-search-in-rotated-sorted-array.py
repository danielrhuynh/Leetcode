class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        L, R = 0, len(nums)-1
        while L <= R:
            M = (L + R) // 2
            if nums[M] == target:
                return M
            if nums[M] >= nums[L]:
                if target > nums[M] or target < nums[L]:
                    L = M+1
                else:
                    R = M
            else:
                if target < nums[M] or target > nums[R]:
                    R = M
                else:
                    L = M+1
        return -1
        