class Solution:
    def snakesAndLadders(self, board):
        linear = [-1]
        reverse = False
        for row in board[::-1]:
            linear += row[::-1] if reverse else row
            reverse = not reverse
        moves = 0
        visited = set()
        queue = {1}
        while queue:
            new_queue = set()
            for i in queue:
                if i in visited or i >= len(linear):
                    continue
                visited.add(i)
                if linear[i] != -1:
                    i = linear[i]
                if i == len(linear) - 1:
                    return moves
                for step in range(1, 7):
                    new_queue.add(i + step)
            moves += 1
            visited |= queue
            queue = new_queue
        return -1
