class Solution:
    def sortColors(self, nums: List[int]) -> None:
        N = len(nums)
        zero,one,two = 0,0,N-1
        while one<=two:
            if zero>one: 
                one = zero
                continue
            if nums[one]==0:
                nums[one],nums[zero] = nums[zero],nums[one]
                zero+=1
                continue
            if nums[one]==2:
                nums[one],nums[two] = nums[two], nums[one]
                two-=1
                continue
            one+=1


            
        