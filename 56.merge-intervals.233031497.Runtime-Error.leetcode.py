# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None:
            return
        ls = len(intervals)
        if ls <= 1:
            return intervals
        # sort by start
        intervals.sort(key=lambda x: x.start)
        pos = 0
        while pos < len(intervals) - 1:
            # check overlap
            if intervals[pos].end >= intervals[pos + 1].start:
                next = intervals.pop(pos + 1)
                # check next is overlap or totally covered by pos
                if next.end > intervals[pos].end:
                    intervals[pos].end = next.end
            else:
                pos += 1
        return intervals
if __name__ == '__main__':
    # begin
    s = Solution()
