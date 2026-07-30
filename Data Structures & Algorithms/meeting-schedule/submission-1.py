"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return True
        intervals.sort(key=lambda interval: interval.start)
        prevMeeting = intervals[0]
        for i in range(1, len(intervals)):
            currentMeeting = intervals[i]
            print(currentMeeting.start)
            print(currentMeeting.end)
            if currentMeeting.start < prevMeeting.end:
                print("Inside if condition")
                return False
            prevMeeting = currentMeeting
        return True
