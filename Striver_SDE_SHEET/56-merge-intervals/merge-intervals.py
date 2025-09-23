class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        prev = intervals[0][1]
        start = intervals[0][-0]
        ans = []
        for i in range(1,len(intervals)):
            if intervals[i][0]<=prev: prev = max(intervals[i][1],prev)
            else:
                ans.append([start,prev])
                start = intervals[i][0]
                prev = intervals[i][1]
        ans.append([start,prev])
        return ans