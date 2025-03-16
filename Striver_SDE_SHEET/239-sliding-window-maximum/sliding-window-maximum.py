class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans,q = [],deque()
        for i in range(n):
            if q and i-q[0]+1>k: q.popleft()
            while q and nums[i]>=nums[q[-1]]: q.pop()
            q.append(i)
            if i+1>=k: ans.append(nums[q[0]])
        return ans

            
