class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(mid):
            ans = 0
            for i in ranks: ans+=math.floor(sqrt(mid/i))
            return ans>=cars
        left,right = 1,max(ranks)*(cars**2)
        while left<=right:
            mid = (left+right)//2
            if check(mid): right = mid-1
            else: left = mid+1
        return left
        

