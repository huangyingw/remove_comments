class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
        	return len(nums)
        count = [0 for _ in range(len(nums))]
        result = 1
        count[0] = nums[0]
        for index in range(1, len(nums)):
        	if nums[index] < count[0]:
        		count[0] = nums[index]
         elif nums[index] > count[result-1]:
        		count[result] = nums[index]
          result += 1
         else:
        		left, right = -1, result-1
          while (right-left > 1):
        			mid = (left+right)/2
           if count[mid] >= nums[index]:
        				right = mid
           else:
        				left = mid
          count[right] = nums[index]
        return result
