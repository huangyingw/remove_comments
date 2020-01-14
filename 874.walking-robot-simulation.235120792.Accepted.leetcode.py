class Solution(object):
    def robotSim(self, commands, obstacles):
        NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        position, orientation = (0, 0), NORTH
        max_sqr_distance = 0
        obstacles = {tuple(obstacle) for obstacle in obstacles}
        for command in commands:
            if command == -2:
                orientation = (orientation - 1) % 4
            elif command == -1:
                orientation = (orientation + 1) % 4
            else:
                for _ in range(command):
                    next_position = (position[0] + directions[orientation][0],
                                     position[1] + directions[orientation][1])
                    if next_position in obstacles:
                        break
                    position = next_position
                    max_sqr_distance = max(max_sqr_distance, position[0] ** 2 + position[1] ** 2)
        return max_sqr_distance
