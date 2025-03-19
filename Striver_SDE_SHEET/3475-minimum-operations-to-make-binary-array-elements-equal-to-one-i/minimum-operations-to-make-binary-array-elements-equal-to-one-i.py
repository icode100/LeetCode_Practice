class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count=0
        l = 0
        for r in range(n):
            if nums[r]==0:
                if r+2>=n: return -1
                for j in range(r,r+3):
                    nums[j] = 1-nums[j]
                count+=1
        return count

            