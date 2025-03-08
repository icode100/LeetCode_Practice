class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        current = 0
        for i in range(n):
            if i>current: return False
            current = max(current,i+nums[i])
        return True


                