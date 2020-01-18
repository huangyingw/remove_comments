class Solution(object):
    def topKFrequent(self, nums, k):
        if not nums:
        	return []
        frequency = {}
        for num in nums:
        	if num in frequency:
        		frequency[num] += 1
         else:
        		frequency[num] = 1
        result = []
        import heapq
        heap = []
        for key, value in frequency.iteritems():
       		heapq.heappush(heap, (-value, key))
        for _ in range(k):
       		result.append(heapq.heappop(heap)[1])
        return result
