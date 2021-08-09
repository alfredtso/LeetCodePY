"""Given an array of meeting time intervals intervals where
intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# tag::MeetingRooms

Test1::

    >>> my = Solution()
    >>> intervals = [[0,30],[5,10],[15,20]]
    >>> my.minMeetingRooms(intervals)
    2
    >>> intervals = [[7, 10],[2,4]]
    >>> my.minMeetingRooms(intervals)
    1
    >>> intervals = [[2,15],[36,45],[9,29],[16,23],[4,9]]
    >>> my.minMeetingRooms(intervals)
    2

# end::MeetingRooms
"""

# tag::MeetingRooms
import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # null check
        if not intervals:
            return 0

        # list as heap
        free_rooms = []

        # sort the intervals with starting time
        intervals.sort(key=lambda x: x[0])

        # add the room using the ending time as key
        heapq.heappush(free_rooms, intervals[0][1])

        # for loop for the remaining rooms
        for meeting in intervals[1:]:

            # ending time <= starting time, then can use the same room and update end
            if free_rooms[0] <= meeting[0]:
                heapq.heappop(free_rooms)


            # if not then add the meeting to a new room
            heapq.heappush(free_rooms, meeting[1])

        return len(free_rooms)

# end::MeetingRooms

if __name__ == "__main__":
    import doctest
    doctest.testmod()