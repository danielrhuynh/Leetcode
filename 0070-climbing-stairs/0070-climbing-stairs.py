class Solution:
    def climbStairs(self, n: int) -> int:
        """
        At each point we can choose to take one or two steps
        If we decide to take one step, another permutation can be made by
        making the opposite decision
        If we end up on the n-1 step the next step has to be a single step
        """
        
        """
        Intuition: We basically work backwards, we start from the nth step
        where we could have taken 1 or 2 steps to get there.
        Our base cases are that we are on the 1st stair (1 way to get there),
        or the 2nd stair (2 ways to get there)
        
        By summing up the ways to reach the n-1 and n-2 stairs, we can find the
        number of ways to climb the set of stairs
        """
        one_step, two_step = 1, 1
        for i in range(n-1):
            temp = one_step
            one_step = one_step + two_step
            two_step = temp
        return one_step
        
        