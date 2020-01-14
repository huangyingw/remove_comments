class Solution(object):
    def superpalindromesInRange(self, L, R):
        L_sqrt = int(int(L) ** 0.5)
        R_sqrt = int((int(R) + 1) ** 0.5)
        digits = [str(i) for i in range(10)]
        def is_palindrome(i):
            return str(i) == str(i)[::-1]
        prev_palis, palis = [""], digits[:]
        result = sum(L_sqrt <= i <= R_sqrt and is_palindrome(i ** 2) for i in range(10))
        for _ in range(2, 11):
            new_palis = []
            for digit in digits:
                for pal in prev_palis:
                    new_pal = digit + pal + digit
                    new_palis.append(new_pal)
                    if new_pal[0] == "0":
                        continue
                    num = int(new_pal)
                    if num > R_sqrt:
                        return result
                    if L_sqrt <= num and is_palindrome(num ** 2):
                        result += 1
            prev_palis, palis = palis, new_palis
