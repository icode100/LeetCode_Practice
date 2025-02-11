class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x:(x[0],-x[1]))
        lis = list()
        for h,w in envelopes:
            i = bisect_left(lis,w)
            if i==len(lis):
                lis.append(w)
            else:
                lis[i] = w
        return len(lis)

