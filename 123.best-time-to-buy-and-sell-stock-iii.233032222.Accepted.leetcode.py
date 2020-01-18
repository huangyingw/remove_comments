class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
        	return 0
        dp = [[0 for _ in range(len(prices))] for _ in range(3)]
        for i in range(1, 3):
        	maxDiff = -prices[0]
         for j in range(1,len(prices)):
        		dp[i][j] = max(dp[i][j-1], prices[j] + maxDiff)
          maxDiff = max(maxDiff, dp[i-1][j] -prices[j])
        return dp[2][len(prices)-1]
