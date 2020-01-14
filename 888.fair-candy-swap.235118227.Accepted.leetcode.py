class Solution(object):
    def fairCandySwap(self, A, B):
        A_candy, B_candy = sum(A), sum(B)
        difference = (A_candy - B_candy) // 2
        B_set = set(B)
        for a in A:
            if a - difference in B_set:
                return [a, a - difference]
        return []
