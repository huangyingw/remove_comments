class Solution:
    def isPerfectSquare(self, num):
        low = 1
        high = num
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def isPerfectSqure(self, num):
    	i = 1
     while num > 0:
    		num -= i
      i += 2
     return num==0
