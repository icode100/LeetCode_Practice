class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def check(mid):
            hour = 0
            for i in range(n):
                if piles[i]<=mid:
                    hour+=1
                else:
                    hour+=(piles[i]//mid)+(1 if piles[i]%mid!=0 else 0)
            return hour<=h
        left,right = 1,max(piles)
        while left<=right:
            mid = (left+right)//2
            if check(mid):right = mid-1
            else: left = mid+1
        return left
