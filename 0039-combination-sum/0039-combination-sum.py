class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total_sum):
                # Base cases
                if total_sum == target:
                    res.append(curr.copy())
                    return
                if i >= len(candidates) or total_sum > target:
                    return
                # Recursive step, 2 decisions to make
                curr.append(candidates[i])
                # Decision where we include the current value
                dfs(i, curr, total_sum + candidates[i])
                # Clean up current decision and travel down branch where the current value cannot be chosen anymore
                curr.pop()
                dfs(i+1, curr, total_sum)
        dfs(0, [], 0)
        return res
            
                