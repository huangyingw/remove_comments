class TwoSum(object):
    def __init__(self):
        self.value_count = {}

    def add(self, number):
        if number in self.value_count:
        	self.value_count[number] += 1
        else:
        	self.value_count[number] = 1

    def find(self, value):
        for val in self.value_count:
        	diff = value - val
         if diff in self.value_count and (diff != val or self.value_count[val] > 1):
        		return True
        return False
