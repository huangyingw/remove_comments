class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for index in range(len(s)):
        	for j in range(i, -1, -1):
        		if dp[j] and s[j:i + 1] in wordDict:
        			dp[i + 1] = True
           break
        return dp[len(s)]
