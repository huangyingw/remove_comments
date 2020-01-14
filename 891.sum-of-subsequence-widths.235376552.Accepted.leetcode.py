class Solution(object):
    def sumSubseqWidths(self, A):
        result = 0
        n = len(A)
        A.sort()
        for i, num in enumerate(A):
            result += (1 << i) * num
            result -= (1 << (n - 1 - i)) * num
        return result % (10 ** 9 + 7)
