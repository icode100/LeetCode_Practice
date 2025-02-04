class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],-x[1]))
        ans = list()
        ans.append(intervals[0])
        i = 1
        while i<len(intervals):
            while i<len(intervals) and intervals[i][0]==ans[-1][0]: i+=1
            if i<len(intervals) and intervals[i][1]<=ans[-1][1]: i+=1
            if i<len(intervals) and intervals[i][1]>ans[-1][1]:
                ans.append(intervals[i])
                i+=1
        # print(intervals)
        # print(ans)
        return len(ans)