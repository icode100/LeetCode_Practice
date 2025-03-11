class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        hashmap,ans,current = {},0,0
        for n in nums:
            current+=n
            if current==k: ans+=1
            ans+=hashmap.get(current-k,0)
            hashmap[current] = hashmap.get(current,0)+1
        return ans