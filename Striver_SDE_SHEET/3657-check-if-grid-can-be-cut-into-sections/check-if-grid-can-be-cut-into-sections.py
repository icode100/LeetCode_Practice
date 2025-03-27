class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x,y = [[r[0],r[2]] for r in rectangles], [[r[1],r[3]] for r in rectangles]
        def function(intervals):
            intervals.sort()
            prev = -1
            count = 0
            for s,e in intervals:
                if s>=prev:
                    count+=1
                prev = max(prev,e)
            return count>=3

        return function(x) or function(y)