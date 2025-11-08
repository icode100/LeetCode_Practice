class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        prefix = [sum(nums[:k])]
        for i in range(k,N): prefix.append(prefix[-1]-nums[i-k]+nums[i])
        @cache
        def recursion(index,count):
            if index>N-k or count<=0: return 0
            return max(recursion(index+1,count), prefix[index]+recursion(index+k,count-1))
        i = 0
        ans = list()
        while i<=N-k and len(ans)<3:
            pick,notpick = prefix[i]+recursion(i+k,3-len(ans)-1), recursion(i+1,3-len(ans))
            if pick>=notpick: 
                ans.append(i)
                i+=k
            else: i+=1
        return  ans


        
            
