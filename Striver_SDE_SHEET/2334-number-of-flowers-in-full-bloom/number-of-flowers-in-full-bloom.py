class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        difference = SortedDict()
        for s,e in flowers:
            difference[s]=difference.get(s,0)+1
            difference[e+1]=difference.get(e+1,0)-1
        pos = list()
        prefix = [0]
        for k,v in difference.items():
            pos.append(k)
            prefix.append(prefix[-1]+v)
        return [prefix[bisect_right(pos,i)] for i in people]


        