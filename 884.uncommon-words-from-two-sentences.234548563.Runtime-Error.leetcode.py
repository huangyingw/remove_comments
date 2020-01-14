class Solution:
    def uncommonFromSentences1(self, A, B):
        from collections import Counter
        mapping = Counter(A.split() + B.split())
        return [m[0] for m in mapping.items() if m[1] == 1]
    def uncommonFromSentences2(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1
        return [word for word in count if count[word] == 1]
