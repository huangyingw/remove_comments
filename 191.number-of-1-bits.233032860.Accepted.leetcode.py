class Solution(object):
    def hammingWeight(self, n):
        bits = 0
        mask = 1
        for i in range(32):
        	if (n & mask) != 0:
        		bits += 1
         mask <<= 1
        return bits
