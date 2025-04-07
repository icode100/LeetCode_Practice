class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        if total&1: return False
        target = total//2
        mask = 1<<nums[0]
        for i in range(1,N):
            mask = (mask<<nums[i])|mask
            mask |= 1<<nums[i]
            if mask&(1<<target): return True
        return False
            
                