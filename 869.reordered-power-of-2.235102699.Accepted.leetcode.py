from math import ceil, log
from collections import Counter


class Solution(object):
    def reorderedPowerOf2(self, N):
        digit_count = Counter(str(N))
        len_N = len(str(N))
        power_of_two = 2 ** int(ceil(log(10 ** (len_N - 1), 2)))
        str_power_of_two = str(power_of_two)
        while len(str_power_of_two) == len_N:
            if Counter(str_power_of_two) == digit_count:
                return True
            power_of_two *= 2
            str_power_of_two = str(power_of_two)
        return False
