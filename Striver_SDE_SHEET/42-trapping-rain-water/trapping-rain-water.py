class Solution:
    def trap(self, height: List[int]) -> int:
        left = [-inf]
        right = deque([-inf])
        N = len(height)
        current = -1
        for i in range(1,N):
            left.append(max(left[-1],height[i-1]))
        for i in range(N-2,-1,-1):
            right.appendleft(max(right[0],height[i+1]))
        ans = 0
        for i in range(N):
            ans+=max(0, min(left[i],right[i])-height[i])
        return ans


