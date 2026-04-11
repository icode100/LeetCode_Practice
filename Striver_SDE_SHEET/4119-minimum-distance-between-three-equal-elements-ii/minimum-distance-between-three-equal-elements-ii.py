class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        N = len(nums)
        ans = inf
        for i in range(N):
            hashmap[nums[i]].append(i)
            maplist = hashmap[nums[i]]
            if len(hashmap[nums[i]])>=3:
                ans = min(
                    ans,
                    (maplist[-1]-maplist[-2])+(maplist[-2]-maplist[-3])+(maplist[-1]-maplist[-3])
                )
        return ans if ans!=inf else -1