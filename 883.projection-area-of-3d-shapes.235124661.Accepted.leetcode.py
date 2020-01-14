class Solution(object):
    def projectionArea(self, grid):
        n = len(grid)
        row_heights, col_heights = [0] * n, [0] * n
        base_area = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] != 0:
                    base_area += 1
                row_heights[row] = max(row_heights[row], grid[row][col])
                col_heights[col] = max(col_heights[col], grid[row][col])
        return base_area + sum(row_heights) + sum(col_heights)
