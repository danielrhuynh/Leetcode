class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine all arrays by zipping
        n = len(startTime)
        jobs = list(zip(startTime, endTime, profit))
        # Sort by starting time
        jobs.sort()
        # Write a recursive method that takes either the first job + next starting time or you skip the job
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0 # no profit to be taken
            # Take the job
            j = i+1
            while j < n and jobs[i][1] > jobs[j][0]:
                j += 1
            first = jobs[i][2]+dfs(j)
            # Pass the job
            second = dfs(i+1)
            return max(first, second)
        return dfs(0)