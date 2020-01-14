class Solution:
    def numPermsDISequence(self, S):
        dp = [1] * (len(S) + 1)
        for move in S:
            if move == "D":
                dp = dp[1:]
                for i in range(len(dp) - 2, -1, -1):
                    dp[i] += dp[i + 1]
            else:
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
        return dp[0] % (10 ** 9 + 7)
