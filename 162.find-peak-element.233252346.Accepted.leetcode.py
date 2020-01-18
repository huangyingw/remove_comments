class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
        	mid = (left + right) / 2
         if nums[mid] > nums[mid+1]:
        		right = mid
         else:
        		left = mid + 1
        return left
class Solution(object):
    def findPeakElement(self, nums):
        left = [False]*len(nums)
        right = [False]*len(nums)
        left[0], right[len(nums)-1] = True, True
        for index in range(1, len(nums)):
            if nums[index] > nums[index-1]:
                left[index] = True
        for index in range(len(nums)-2, -1, -1):
            if nums[index] > nums[index+1]:
                right[index] = True
        for index in range(len(left)):
            if left[index] and right[index]:
                return index
        return -1
