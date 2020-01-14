class Solution(object):
    def advantageCount(self, A, B):
        B_i = sorted([(b, i) for i, b in enumerate(B)])
        result = [None] * len(A)
        i = 0
        for a in sorted(A):
            if a > B_i[i][0]:
                result[B_i[i][1]] = a
                i += 1
            else:
                result[B_i.pop()[1]] = a
        return result
