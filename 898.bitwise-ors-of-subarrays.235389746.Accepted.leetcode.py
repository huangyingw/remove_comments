class Solution(object):
    def subarrayBitwiseORs(self, A):
        all_or, subarray_or = set(), set()
        for num in A:
            new_or = {num | x for x in subarray_or}
            new_or.add(num)
            all_or |= new_or
            subarray_or = new_or
        return len(all_or)
