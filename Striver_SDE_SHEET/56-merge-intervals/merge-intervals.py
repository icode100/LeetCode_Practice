class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = list()
        mini = intervals[0][0]
        maxi = intervals[0][1]
        i = 1
        while i<n:
            if intervals[i][0]>maxi:
                ans.append([mini,maxi])
                mini = intervals[i][0]
                maxi = intervals[i][1]
            else:
                mini = min(mini,intervals[i][0])
                maxi = max(maxi,intervals[i][1])
            i+=1
        ans.append([mini,maxi])
        return ans

        