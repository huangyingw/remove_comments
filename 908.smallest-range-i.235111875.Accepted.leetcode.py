class Solution:
    def smallestRangeI(self, A, K):
        range = max(A) - min(A)
        return max(0, range - 2 * K)
