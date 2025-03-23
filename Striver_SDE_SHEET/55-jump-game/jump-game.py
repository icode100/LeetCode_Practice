class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_i = 0
        for i in range(n):
            if i>max_i: return False
            max_i = max(max_i,i+nums[i])
        return True
                


                