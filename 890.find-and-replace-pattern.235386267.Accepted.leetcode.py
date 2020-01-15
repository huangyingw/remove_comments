from collections import defaultdict


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def canonical(s):
            result = []
            mapping = {}
            value = 0
            for c in s:
                if c not in mapping:
                    mapping[c] = value
                    value += 1
                result.append(mapping[c])
            return tuple(result)
        pattern = canonical(pattern)
        return [word for word in words if canonical(word) == pattern]
