class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(set)
        bookkeeping = defaultdict(int)
        ans = list()
        for ball,col in queries:
            if ball in bookkeeping:
                colors[bookkeeping[ball]].remove(ball)
                if len(colors[bookkeeping[ball]])==0: colors.pop(bookkeeping[ball])
                bookkeeping[ball] = col
                colors[col].add(ball)
            else:
                bookkeeping[ball] = col
                colors[col].add(ball) 
            ans.append(len(colors))
        return ans

