class Solution(object):
    def increasingTriplet(self, nums):
        first, second = float('inf'), float('inf')
        for val in nums:
        	if val <= first:
        		first = val
         elif val <= second:
        		second = val
         else:
        		return True
        return False
