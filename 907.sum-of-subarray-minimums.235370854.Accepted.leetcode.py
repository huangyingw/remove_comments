class Solution:
    def sumSubarrayMins(self, A):
        A = [float("-inf")] + A + [float("-inf")]
        result = 0
        stack = []
        for i, num in enumerate(A):
            while stack and num < A[stack[-1]]:
                j = stack.pop()
                result += A[j] * (j - stack[-1]) * (i - j)
            stack.append(i)
        return result % (10 ** 9 + 7)
