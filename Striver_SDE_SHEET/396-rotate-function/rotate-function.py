class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        current = 0
        inc = 0
        for i,num in enumerate(nums):
            current+=(i*num)
            inc+=num
        ans = current
        for k in range(1,n):
            current = current+inc-(nums[-k]*n)
            ans = max(ans,current)
        return ans

            
            