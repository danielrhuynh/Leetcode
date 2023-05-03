class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            maxProfit = max(maxProfit, prices[i]-prices[buy])
        return maxProfit
            