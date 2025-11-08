class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        prefix = [0]+list(accumulate(nums))

        @cache
        def recursion(i,M):
            if M==0 or i>N-k: return 0
            pick = (prefix[i+k]-prefix[i])+recursion(i+k,M-1)
            notpick = recursion(i+1,M)
            return max(pick,notpick)
        
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
        
            
