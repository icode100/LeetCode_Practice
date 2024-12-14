class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        function =lambda l,r: (r-l)*min(height[l],height[r])
        ans = function(l,r)
        while l<=r:
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            ans = max(ans,function(l,r))
        return ans
            