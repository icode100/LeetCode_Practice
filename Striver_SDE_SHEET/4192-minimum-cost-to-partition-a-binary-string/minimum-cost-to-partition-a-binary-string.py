class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        X = s.count('1')
        L = len(s)
        if len(s)&1:
            if X==0:return flatCost
            return L*X*encCost
        
        prefix = [0]
        for c in s:
            prefix.append(prefix[-1]+int(c))
        prefix.pop(0)
        # print(prefix)
        def recursion(l,r):
            L = r-l+1
            X = prefix[r]-(prefix[l-1] if l>0 else 0)
            cost = L*X*encCost if X>0 else flatCost
            if L==2: return min(cost,recursion(l,l)+recursion(r,r))
            mid = (l+r)//2
            if L&1==0:
                cost = min(
                    cost,
                    recursion(l,mid)+recursion(mid+1,r)
                )
            return cost
        return recursion(0,L-1)
            