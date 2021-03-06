class Solution(object):
    def largestRectangleArea(self, heights):
        if not heights:
        	return 0
        stack = []
        result, index = 0, 0
        while index < len(heights):
        	if not stack or heights[index] >= heights[stack[-1]]:
        		stack.append(index)
          index += 1
         else:
        		curr = stack.pop()
          if not stack:
        			area = heights[curr]*index
          else:
        			area = heights[curr] * (index-stack[-1]-1)
          result = max(result, area)
        while stack:
        	curr = stack.pop()
         if not stack:
        		area = heights[curr]*index
         else:
        		area = heights[curr] * (index-stack[-1]-1)
         result = max(result, area)
        return result
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0 for index in range(n)]
        result = 0
        for index_i in range(m):
            for index_j in range(n):
                if matrix[index_i][index_j] != '0':
                    heights[index_j] = heights[index_j] + 1
                else:
                    heights[index_j] = 0
            result = max(result, self.largestRectangleArea(heights))
        return result
