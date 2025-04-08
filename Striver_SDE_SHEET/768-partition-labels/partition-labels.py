class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexer = {}
        for i,c in enumerate(s[::-1]):
            if c not in indexer: indexer[c] = len(s)-i-1
        ans,bound = [],0
        for i,c in enumerate(s):
            if bound<i: ans.append(i)
            bound = max(bound,indexer[c])
        ans.append(i+1)
        return [ans[0]]+[ans[i]-ans[i-1] for i in range(1,len(ans))]
        

