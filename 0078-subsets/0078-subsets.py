class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        # i is the index of the value we are making the decision on
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            # decision to include nums[i]
            curr.append(nums[i])
            dfs(i+1)
            
            # decision to not include nums[i]
            curr.pop()
            dfs(i+1)
        dfs(0)
        return res
            
            
            
            
            