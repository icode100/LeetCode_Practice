class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        one = 0
        two = len(nums)-1
        while one<=two:
            if nums[one]==0:
                nums[one],nums[zero] = nums[zero],nums[one]
                one+=1
                zero+=1
            elif nums[one]==2:
                nums[two],nums[one] = nums[one],nums[two]
                two-=1
            elif nums[one]==1:
                one+=1