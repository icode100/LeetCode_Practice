class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = defaultdict(int)
        mod = int(1e9+7)
        for num in nums:
            count[num] = (count[num]+count[num-1]+count[num+1]+1)%mod
            ans[num] = (ans[num]+ans[num-1]+ans[num+1]+num*(count[num-1]+count[num+1]+1))%mod
        return sum(ans.values())%mod