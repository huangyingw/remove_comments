class RLEIterator(object):
    def __init__(self, A):
        self.encoding = A
        self.length = len(A)
        self.i = 0
    def next(self, n):
        while self.i < self.length and self.encoding[self.i] < n:
            n -= self.encoding[self.i]
            self.i += 2
        if self.i >= self.length:
            return -1
        self.encoding[self.i] -= n
        return self.encoding[self.i + 1]
