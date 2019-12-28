"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        temp = []
        for interval in intervals:
            a, d = interval.start, interval.end
            temp += [(a, 1), (d, -1)]
        temp.sort()
        #print(temp)
        res, num = 0, 0
        for t in temp:
            num += t[1]
            res = max(res, num)
        
        return res
