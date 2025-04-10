class Solution:
    def sortColors(self, nums: List[int]) -> None:
        N = len(nums)
        l,r,e = 0,0,N-1
        while r<=e:
            if l>r:
                r = l
                continue
            if nums[r]==0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                continue
            elif nums[r]==2:
                nums[e],nums[r] = nums[r],nums[e]
                e-=1
                continue
            r+=1
        return 


        