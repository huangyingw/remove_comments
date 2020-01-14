_author_ = 'jake'
_project_ = 'leetcode'
# https://leetcode.com/problems/strange-printer/
# There is a strange printer with the following two special requirements:
# original existing characters.
# Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer
# First remove repeated characters since they will always be printed together.
# same time in either case. So we can split the subproblems at every char that is the same as the starting char and
# take the minimum prints of all those split points.
# Time - O(n**3), iterate over every of the n**2 substrings
# Space - O(n**2)


class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = "".join([a for a, b in zip(s, "#" + s) if a != b])  # remove repeated chars
        memo = {}

        def helper(i, j):
            if j - i + 1 <= 1:                  # length <= 1, return length
                return j - i + 1
            if (i, j) in memo:
                return memo[(i, j)]
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:                # all chars that match first
            memo[(i, j)] = min_prints
            return min_prints
        return helper(0, len(s) - 1)
