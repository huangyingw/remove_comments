class Solution(object):
	def maxKilledEnemies(self, grid):
		if not grid or len(grid) == 0 or len(grid[0]) == 0:
			return 0
  result, row_count = float('-inf'), 0
  column_count = [0]*len(grid[0])
  for row in range(len(grid)):
			for column in range(len(grid[0])):
				if column == 0 or grid[row][column-1] == 'W':
					row_count = 0
     for index in range(column, len(grid[0])):
						if grid[row][index] == 'W':
							break
      row_count += 1 if grid[row][index] == 'E' else 0
    if row == 0 or grid[row-1][column] == 'W':
					column_count[column] = 0
     for index in range(row, len(grid)):
						if grid[index][column] == 'W':
							break
      column_count[column] += 1 if grid[index][column] == 'E' else 0
    if grid[row][column] == '0':
					result = max(result, row_count + column_count[column])
  return result
grid = [['0', 'E', '0', '0'],
['E', '0', 'W', 'E'],
['0', 'E', '0', '0']]
