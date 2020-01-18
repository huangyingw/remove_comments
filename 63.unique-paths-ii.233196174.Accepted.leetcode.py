class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
        	return 0
        dp[0][0] = 1
        for index in range(1, m):
        	if obstacleGrid[index][0] == 1:
        		dp[index][0] = 0
         else:
        		dp[index][0] = dp[index-1][0]
        for index in range(1, n):
        	if obstacleGrid[0][index] == 1:
        		dp[0][index] = 0
         else:
        		dp[0][index] = dp[0][index-1]
        for index_i in range(1, m):
        	for index_j in range(1, n):
        		if obstacleGrid[index_i][index_j] == 1:
        			dp[index_i][index_j] = 0
          else:
        			dp[index_i][index_j] = dp[index_i-1][index_j] + dp[index_i][index_j-1]
        return dp[m-1][n-1]
