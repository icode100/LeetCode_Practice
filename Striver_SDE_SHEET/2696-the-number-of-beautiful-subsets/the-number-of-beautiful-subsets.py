class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        def dfs(index,vis):
            if index>=N: return 0 if not vis else 1
            # notpick
            notpick = dfs(index+1,vis)
            # pick
            pick = 0
            if nums[index]-k not in vis:
               pick = dfs(index+1,vis|{nums[index]})
            return pick+notpick
        return dfs(0,set())

            


