class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = list()
        intervals.sort()
        for s,e in intervals:
            if not ans or s>ans[-1][1]: ans.append([s,e])
            else: ans[-1][1] = max(e,ans[-1][1])
        return ans