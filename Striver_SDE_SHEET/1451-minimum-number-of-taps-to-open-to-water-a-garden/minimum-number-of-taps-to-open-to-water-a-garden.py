class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        maxrange = [0]*(n+1)
        for i,num in enumerate(ranges): maxrange[max(0,i-num)] = max(maxrange[max(0,i-num)],min(n,i+num))
        next = 0
        ans = 1
        best = maxrange[0]
        for i,num in enumerate(maxrange):
            if best == n: return ans
            if i>best: return -1
            if i==best:
                ans+=1
                next = max(next,maxrange[i])
                best = next
                next = 0
            else: next = max(next,maxrange[i])
        return ans
            


                
            
        
