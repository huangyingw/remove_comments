class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
        	return 0
        if len(s) == 1:
        	return 1
        dp = [0] * len(s)
        dp[0] = 1
        if int(s[:2]) > 26:
        	if s[1] != '0':
        		dp[1] = 1
         else:
        		dp[0] = 0
        else:
        	if s[1] != '0':
        		dp[1] = 2
         else:
        		dp[1] = 1
        for index in range(2, len(s)):
        	if s[index] != '0':
        		dp[index] += dp[index-1]
         val = int(s[index-1:index+1])
         if val >= 10 and val <= 26:
        		dp[index] += dp[index-2]
        return dp[len(s)-1]
