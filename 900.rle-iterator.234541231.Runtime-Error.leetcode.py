class RLEIterrator():
    def __init__(self, A):
        self.inputList = A
    def next(self, n):
        index = 0
        while index < len(self.inputList):
            if self.inputList[index] == 0:
                self.inputList = self.inputList[index + 2:]
            elif n <= self.inputList[index]:
                output = self.inputList[index + 1]
                self.inputList[index] -= n
                return output
            else:
                n -= self.inputList[index]
                self.inputList = self.inputList[index + 2:]
        if n > 0:
            return -1
