class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                index = i
                break
        if index==-1: 
           nums.reverse()
           return 
        for i in range(len(nums)-1,index-1,-1):
            if nums[index]<nums[i]:
                nums[index],nums[i] = nums[i],nums[index]
                break
        nums[::1] = nums[:index+1]+nums[index+1:][::-1]
        