class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        prev = points[0][1]
        count = 1
        for i,j in points:
            if i>prev:
                count+=1
                prev = j
        return count