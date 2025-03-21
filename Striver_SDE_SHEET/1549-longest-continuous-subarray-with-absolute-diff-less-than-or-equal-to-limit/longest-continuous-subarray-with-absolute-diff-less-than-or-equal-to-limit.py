class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque()
        min_q = deque()
        n = len(nums)
        l = 0
        ans = 0
        for r in range(n):
            while max_q and nums[r]>nums[max_q[-1]]:
                max_q.pop()
            while min_q and nums[r]<nums[min_q[-1]]:
                min_q.pop()
            max_q.append(r)
            min_q.append(r)
            while nums[max_q[0]]-nums[min_q[0]]>limit:
                if l==max_q[0]: max_q.popleft()
                if l==min_q[0]: min_q.popleft()
                l+=1
            ans = max(ans,r-l+1)
        return ans

