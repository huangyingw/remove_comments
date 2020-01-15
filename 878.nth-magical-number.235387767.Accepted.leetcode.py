class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        low, high = 1, 10 ** 14

        def gcd(a, b):
            a, b = b, a % b
            if b == 0:
                return a
            return gcd(a, b)
        lcm = A * B // gcd(A, B)
        while low < high:
            mid = (low + high) // 2
            num = (mid // A) + (mid // B) - (mid // lcm)
            if num < N:
                low = mid + 1
            elif num >= N:
                high = mid
        return low % (10 ** 9 + 7)
