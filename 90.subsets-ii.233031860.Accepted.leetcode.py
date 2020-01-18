class Solution(object):
    def subsetsWithDup(self, nums):
        result = [[]]
        for num in nums:
        	for index in range(len(result)):
        		new_list = result[index] + [num]
          new_list.sort()
          result.append(new_list)
        unique = set(tuple(val) for val in result)
        return list(list(val) for val in unique)
