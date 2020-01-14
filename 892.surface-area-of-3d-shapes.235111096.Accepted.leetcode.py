class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        area = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                height = grid[row][col]
                area += 4 * height + 2
                if row != 0:
                    area -= min(grid[row - 1][col], height)
                if col != 0:
                    area -= min(grid[row][col - 1], height)
                if row != n - 1:
                    area -= min(grid[row + 1][col], height)
                if col != n - 1:
                    area -= min(grid[row][col + 1], height)
        return area
