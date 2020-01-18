class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        while True:
        	slow = nums[slow]
         fast = nums[nums[fast]]
         if slow == fast:
        		break
        num1= nums[0]
        num2 = slow
        while num1 != num2:
        	num1 = nums[num1]
         num2 = nums[num2]
        return num2
