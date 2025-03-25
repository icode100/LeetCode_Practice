class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dp_1, dp_2, dp = {},{},{}
        for x in nums:
            if x-1 in dp_1:
                dp_2[x] = dp_2.get(x,0)+1
                dp_1[x-1]-=1
                if dp_1[x-1] == 0: dp_1.pop(x-1)
            elif x-1 in dp_2:
                dp[x] = dp.get(x,0)+1
                dp_2[x-1]-=1
                if dp_2[x-1]==0: dp_2.pop(x-1)
            elif x-1 in dp:
                dp[x-1]-=1
                dp[x] = dp.get(x,0)+1
                if dp[x-1]==0: dp.pop(x-1)
            else: dp_1[x] = dp_1.get(x,0)+1
        if len(dp_1)>0 or len(dp_2)>0: return False
        return True