class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        bookkeeping = defaultdict(int)
        ans = list()
        for ball,col in queries:
            if ball in bookkeeping:
                colors[bookkeeping[ball]]-=1
                if colors[bookkeeping[ball]]==0: colors.pop(bookkeeping[ball])
                bookkeeping[ball] = col
                colors[col]+=1
            else:
                bookkeeping[ball] = col
                colors[col]+=1
            ans.append(len(colors))
        return ans

