class Solution(object):
	def shortestDistance(self, grid):
		if not grid:
			return -1
  def bfs(grid, distance_reach_map, row, col):
			if(row < 0 or row > len(grid) or col < 0 or col > len(grid[0])):
				return
   queue = [[row, col]]
   qdist = [1]
   direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
   while queue:
				x, y = queue.pop(0)
    curr_dist = qdist.pop(0)
    for dx, dy in direction:
					new_x, new_y = x+dx, y+dy
     if((0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])) and grid[new_x][new_y] == 0):
						grid[new_x][new_y] = -1
      queue.append([new_x, new_y])
      temp = distance_reach_map[new_x][new_y]
      dist, reach = temp[0], temp[1]
      dist += curr_dist
      reach += 1
      distance_reach_map[new_x][new_y] = [dist, reach]
      qdist.append(curr_dist+1)
   for row in range(len(grid)):
				for col in range(len(grid[0])):
					if grid[row][col] == -1:
						grid[row][col] =0
  r_len, c_len = len(grid), len(grid[0])
  distance_reach_map = [[[0, 0]]*c_len for _ in range(r_len)]
  buildings = 0
  for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] == 1:
					bfs(grid, distance_reach_map, row, col)
     buildings += 1
  result = float('inf')
  for row in range(r_len):
			for col in range(c_len):
				dist, reach = distance_reach_map[row][col]
    if reach == buildings:
					result = min(result, dist)
  return result
grid = [[1, 0, 2, 0, 1], 
  [0, 0, 0, 0, 0], 
  [0, 0, 1, 0 ,0]]
