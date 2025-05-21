class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j-i != nums[j]-nums[i] => nums[i]-i != nums[j]-j
        N = len(nums)
        hashmap = {}
        for i in range(N): hashmap[nums[i]-i] = hashmap.get(nums[i]-i,0)+1
        nc2 = lambda x: (x*(x-1))//2
        ans = nc2(N)
        for val in hashmap.values(): ans-=nc2(val)
        return ans


