from collections import defaultdict


class FreqStack(object):
    def __init__(self):
        self.counter = defaultdict(int)
        self.stack_of_stacks = []

    def push(self, x):
        self.counter[x] += 1
        count = self.counter[x]
        if count > len(self.stack_of_stacks):
            self.stack_of_stacks.append([])
        self.stack_of_stacks[count - 1].append(x)

    def pop(self):
        num = self.stack_of_stacks[-1].pop()
        self.counter[num] -= 1
        if not self.stack_of_stacks[-1]:
            self.stack_of_stacks.pop()
        return num
