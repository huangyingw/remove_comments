class Solution(object):
    def sortColors(self, nums):
        zero, last = 0, len(nums) - 1
        index = 0
        while index <= last:
        	if nums[index] == 1:
        		index += 1
         elif nums[index] == 0:
        		nums[index], nums[zero] = nums[zero], nums[index]
          index += 1
          zero += 1
         elif nums[index] == 2:
        		nums[last], nums[index] = nums[index], nums[last]
          last -= 1
