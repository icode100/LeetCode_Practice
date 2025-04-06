class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        prefix = [0]+list(accumulate(nums))

        dp = {}
        def recursion(i,M):
            if M==0 or i>N-k: return 0
            if (i,M) in dp: return dp[(i,M)]
            pick = (prefix[i+k]-prefix[i])+recursion(i+k,M-1)
            notpick = recursion(i+1,M)
            dp[(i,M)] = max(pick,notpick)
            return dp[(i,M)]
        
        i = 0
        ans = list()
        while i<=N-k and len(ans)<3:
            pick = prefix[i+k]-prefix[i] +recursion(i+k,3-len(ans)-1)
            notpick = recursion(i+1,3-len(ans))
            if pick>=notpick:
                ans.append(i)
                i+=k
            else: i+=1
        return ans
        
            
