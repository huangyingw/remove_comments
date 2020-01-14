class Solution(object):
    def lenLongestFibSubseq(self, A):
        A_set = set(A)
        max_length = 0
        for i, num in enumerate(A):
            for num2 in A[i + 1:]:
                prev_num = num2
                next_num = num + num2
                length = 2
                while next_num in A_set:
                    length += 1
                    next_num, prev_num = next_num + prev_num, next_num
                max_length = max(max_length, length)
        return max_length if max_length >= 3 else 0
