class Solution:
    def numDecodings1(self, s):
        if not s or s == "0":
            return 0
        care, dont = 0, 1
        for i in range(1, len(s)):
            p, c = s[i - 1], s[i]
            if c == "0":
                if not (p == "1" or p == "2"):
                    return 0
                else:
                    care, dont = dont, 0
            elif p == "0":
                care, dont = 0, care
            else:
                if 11 <= int(p + c) <= 26:
                    care, dont = dont, dont + care
                else:
                    care, dont = 0, dont + care
        return dont + care

    def numDecodings2(self, s):
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w
