class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -sys.maxsize-1
        p = 1
        for num in nums:
            if p==0: p=1
            p*=num
            ans = max(ans,p)
        p = 1
        for num in nums[::-1]:
            if p==0: p=1
            p*=num
            ans = max(ans,p)
        return ans