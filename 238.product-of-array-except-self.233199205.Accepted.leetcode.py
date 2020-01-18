class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
        	return []
        dp = [1] * len(nums)
        for index in range(1, len(nums)):
        	dp[index] = dp[index - 1] * nums[index - 1]
        right = 1
        for index in range(len(nums) - 1, -1, -1):
        	dp[index] *= right
         right *= nums[index]
        return dp
