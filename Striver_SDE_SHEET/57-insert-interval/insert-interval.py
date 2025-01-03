class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = list()
        i = 0
        # adding intervals prior to newInterval
        while i<n and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i+=1
        #performing merge interval on merging intervals with overlapping intervals with newInterval
        while i<n and newInterval[1]>=intervals[i][0]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i+=1
        ans.append(newInterval)
        # push remaining intervals
        while i<n:
            ans.append(intervals[i])
            i+=1
        return ans 


