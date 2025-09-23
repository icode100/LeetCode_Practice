class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        check = 0
        for i in range(len(nums)):
            if count == 0:
                count+=1
                check = nums[i]
            elif nums[i]==check: count+=1
            else: count-=1
        return check