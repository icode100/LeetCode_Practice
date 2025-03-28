class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = list()
        d = SortedDict()
        for s,e in intervals:
            d[s] = d.get(s,0)+1
            d[e] = d.get(e,0)-1
        start = 0
        count = 0
        for k,v in d.items():
            if count==0: start = k
            count+=v
            if count == 0: ans.append([start,k])
        return ans

