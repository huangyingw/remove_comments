class Solution(object):
    def numSquares(self, n):
        mapping = {}
        squares = [num * num for num in range(1, int(pow(n, 0.5)) + 1)]
        for square in squares:
        	mapping[square] = 1
        for val in range(1, n + 1):
        	if val not in mapping:
        		mapping[val] = float('inf')
          for square in squares:
        			if square < val:
        				mapping[val] = min(mapping[val], mapping[square] + mapping[val-square])
        return mapping[n]
