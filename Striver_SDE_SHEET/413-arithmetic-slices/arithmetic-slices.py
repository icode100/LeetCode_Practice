class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N,ans,current = len(nums),0,0
        count = 0
        if N<3: return 0
        current = nums[1]-nums[0]
        for r in range(2,N):
            if nums[r]-nums[r-1]==current: 
                count +=1
                ans+=count
            else: 
                current = nums[r]-nums[r-1]
                count=0
        return ans
            
