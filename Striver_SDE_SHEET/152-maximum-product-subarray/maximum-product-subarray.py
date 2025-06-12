class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf
        current = 1
        for i,num in enumerate(nums):
            if current==0: current = 1
            current*=num
            ans = max(current,ans)
        current = 1
        for i,num in enumerate(nums[::-1]):
            if current==0: current = 1
            current*=num
            ans = max(current,ans)
        return ans