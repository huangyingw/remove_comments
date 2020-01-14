import heapq
from collections import defaultdict
class Solution(object):
    def reachableNodes(self, edges, M, N):
        adjacency = defaultdict(set)
        subdivisions = {}
        for a, b, intermediate in edges:
            subdivisions[(a, b)] = [intermediate, 0]
            subdivisions[(b, a)] = [intermediate, 0]
            adjacency[a].add((b, intermediate))
            adjacency[b].add((a, intermediate))
        queue = [(0, 0)]
        visited = set()
        while queue and len(visited) < N:
            steps, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            for nbor, distance in adjacency[node]:
                subdivisions[(node, nbor)][1] = min(distance, M - steps)
                if steps + distance + 1 <= M:
                    heapq.heappush(queue, (steps + distance + 1, nbor))
        result = len(visited)
        for (a, b), (distance, covered) in subdivisions.items():
            if a < b:
                result += min(distance, covered + subdivisions[(b, a)][1])
        return result
