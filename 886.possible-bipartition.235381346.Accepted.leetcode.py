from collections import defaultdict
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        dislike = defaultdict(set)
        for a, b in dislikes:
            dislike[a].add(b)
            dislike[b].add(a)
        this, other = set(), set()
        for i in range(1, N + 1):
            if i in this or i in other:
                continue
            to_add = {i}
            while to_add:
                this |= to_add
                disliked = set()
                for num in to_add:
                    disliked |= dislike[num]
                if disliked & this:
                    return False
                disliked -= other
                to_add = disliked
                this, other = other, this
        return True
