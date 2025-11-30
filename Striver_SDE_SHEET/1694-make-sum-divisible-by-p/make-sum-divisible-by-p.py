class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        current = 0
        hashmap = defaultdict(int)
        total = sum(nums)
        if total%p == 0: return 0
        mod = total%p
        ans = N

        for i,num in enumerate(nums):
            current += num
            currmod = current%p
            checkmod = (current - mod)%p

            if currmod == mod: ans = min(ans,i+1)
            
            if checkmod in hashmap: 
                ans = min(ans,i-hashmap[checkmod])
            
            hashmap[currmod] = i
        
        return ans if ans<N else -1
