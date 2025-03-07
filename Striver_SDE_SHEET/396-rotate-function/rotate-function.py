class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        current = sum([i*nums[i] for i in range(n)])
        inc = sum(nums)
        ans = current
        for k in range(1,n):
            current = current+inc-(nums[-k]*n)
            ans = max(ans,current)
        return ans

            
            