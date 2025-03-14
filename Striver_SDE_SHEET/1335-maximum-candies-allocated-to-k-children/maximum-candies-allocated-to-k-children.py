class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort(reverse = True)
        if sum(candies)<k: return 0
        def check(mid):
            tempk = k
            i = 0
            while tempk>0 and i<len(candies):
                if candies[i]<mid:
                    return False
                else:
                    tempk-=candies[i]//mid
                    i+=1
            return True if tempk<=0 else False
        left,right = 1,sum(candies)
        while left<=right:
            mid = (left+right)>>1
            if check(mid):
                left = mid+1
            else:
                right = mid-1
        # print(left,right)
        return right
            
