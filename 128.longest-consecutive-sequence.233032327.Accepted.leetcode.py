class Solution(object):
    def longestConsecutive(self, nums):
        result = 0
        nums = set(nums)
        for num in nums:
        	if num - 1 not in nums:
        		curr = num
          length = 1
          while curr+1 in nums:
        			curr += 1
           length += 1
          result = max(result, length)
        return result
