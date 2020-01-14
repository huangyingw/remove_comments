class Solution(object):
    def superEggDrop(self, K, N):
        drops = 0
        floors = [0 for _ in range(K + 1)]
        while floors[K] < N:
            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
            drops += 1
        return drops
