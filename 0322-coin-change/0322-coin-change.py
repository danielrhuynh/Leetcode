class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]*(amount+1) # since were going to 0...amount
        dp[0] = 0 # base case
        
        for amount in range(1, amount+1):
            for coin in coins:
                if amount - coin >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount-coin])
        return dp[amount] if dp[amount] != amount+1 else -1