class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
        	return False
        left, right = 0, len(matrix[0]) - 1
        while left < len(matrix) and right >= 0:
        	if matrix[left][right] == target:
        		return True
         elif matrix[left][right] < target:
        		left += 1
         else:
        		right -= 1
        return False
