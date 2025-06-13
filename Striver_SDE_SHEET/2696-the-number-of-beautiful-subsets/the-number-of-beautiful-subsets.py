class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        
        def dfs(index,vis):
            if index>=N: return 0 if vis==0 else 1
            # notpick
            notpick = dfs(index+1,vis)
            # pick
            pick = 0
            if ((nums[index]-k)>=0 and ((1<<(nums[index]-k)) & vis)==0) or ((nums[index]-k)<0):
               pick = dfs(index+1,vis|(1<<(nums[index])))
            return pick+notpick
        return dfs(0,0)

            


