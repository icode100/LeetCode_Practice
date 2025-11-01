class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        dp = [1]*N
        parent = [i for i in range(N)]
        last = 0
        ans = 0
        for i in range(N):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                    # print('hi')
                    dp[i] = dp[j]+1
                    parent[i] = j
            if ans<dp[i]:
                ans = dp[i]
                last = i
        # print(dp)
        ans = list()
        ptr = last
        while ptr!=parent[ptr]:
            ans.append(nums[ptr])
            ptr = parent[ptr]
        ans.append(nums[ptr])
        return ans[::-1]
        
