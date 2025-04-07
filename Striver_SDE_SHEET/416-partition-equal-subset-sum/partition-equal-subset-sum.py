class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        if total&1: return False
        target = total//2
        dp = {0}
        for i in range(N-1,-1,-1):
            temp = set()
            for d in dp:
                if d==target: return True
                temp.add(d+nums[i])
                temp.add(d)
            dp = temp
        return False
            
                