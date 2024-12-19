class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],x[0]))
        limit = intervals[0][1]
        ans = 1
        for start,end in intervals[1:]:
            if start>=limit:
                limit = end
                ans+=1
        return len(intervals)-ans
