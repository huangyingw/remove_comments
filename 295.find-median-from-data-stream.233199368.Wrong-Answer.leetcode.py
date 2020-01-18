import heapq


class MedianFinder(object):
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        if not self.max_heap or num > -self.max_heap[0]:
        	heapq.heappush(self.min_heap, num)
         if len(self.min_heap) > len(self.max_heap) + 1:
        		heapq.heappush(self.max_heap, -heapq.heapop(self.min_heap))
  else:
			heapq.heappush(self.max_heap, -num)
   if len(self.max_heap) > len(self.min_heap):
				heapq.heappush(self.min_heap, -heapq.heapop(self.max_heap))        
    def findMedian(self):
        if len(self.max_heap) == len(self.min_heap):
        	return (-self.max_heap[0]+self.min_heap[0] )/2.0
        else:
        	return self.min_heap[0]
