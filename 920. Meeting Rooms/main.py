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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        temp = [(interval.start, interval.end) for interval in intervals]
        temp.sort()
        for i in range(1, len(temp)):
            if temp[i-1][1] > temp[i][0]:
                return False
        
        return True
