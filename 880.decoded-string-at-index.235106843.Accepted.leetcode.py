class Solution(object):
    def decodeAtIndex(self, S, K):
        length = 0
        for index, c in enumerate(S):
            if "0" <= c <= "9":
                length *= int(c)
            else:
                length += 1
            if length >= K:
                break
        for i in range(index, -1, -1):
            c = S[i]
            if "0" <= c <= "9":
                length //= int(c)
                K %= length
            else:
                if K == length or K == 0:
                    return c
                length -= 1
