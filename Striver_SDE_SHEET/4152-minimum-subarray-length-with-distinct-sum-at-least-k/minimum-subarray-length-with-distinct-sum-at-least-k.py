class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        counter = defaultdict(int)
        ans = inf
        l = 0
        sum = 0
        for r in range(N):
            counter[nums[r]]+=1
            if counter[nums[r]]==1: sum+=nums[r]
            while sum>=k and l<=r:
                ans = min(ans,r-l+1)
                counter[nums[l]]-=1
                if counter[nums[l]]==0:
                    sum-=nums[l]
                l+=1
        return ans if ans<inf else -1

