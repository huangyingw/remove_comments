class Solution(object):
    def findMin(self, nums):
        if not nums:
        	return 0
        if len(nums) == 1:
        	return nums[0]
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
        	return nums[left]
        while left <= right:
        	while nums[left] == nums[right] and left != right:
        		left += 1
         if nums[left] <= nums[right]:
        		return nums[left]
         mid = (left + right)/2
         if nums[mid] >= nums[left]:
        		left = mid+1
         else:
        		right = mid
        return -1
