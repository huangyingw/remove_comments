class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        result = 1
        while self.stack and price >= self.stack[-1][0]:
            _, count = self.stack.pop()
            result += count
        self.stack.append([price, result])
        return result
