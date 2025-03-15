class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def check(mid):
            count = 0
            i = 0
            while i<n:
                if nums[i]<=mid:
                    i+=2
                    count+=1
                else: i+=1
                if count==k: return True
            return False
                
        left,right = min(nums),max(nums)
        while left<=right:
            mid = (left+right)//2
            if check(mid): right = mid-1
            else: left = mid+1
        return left

        
        
