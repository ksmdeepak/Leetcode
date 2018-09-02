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
        if len(intervals)==0:
            return []
        intervals.sort(key=lambda x: x.start)
        for i in intervals:
            print(i.start)
        stack = []
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            temp = stack[len(stack)-1]
            if temp.end >= intervals[i].start and intervals[i].end > temp.end:
                temp.end = intervals[i].end
                stack[len(stack)-1] = temp
            elif temp.end > intervals[i].start and temp.end >= intervals[i].end:
                continue
            elif intervals[i].start > temp.end:
                stack.append(intervals[i])
        return stack