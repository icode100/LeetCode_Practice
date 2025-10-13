class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostK(k):
            ans,l,hashmap = 0,0,defaultdict(int)
            for r,n in enumerate(nums):
                hashmap[n]+=1
                while len(hashmap)>k:
                    hashmap[nums[l]]-=1
                    if hashmap[nums[l]]==0: hashmap.pop(nums[l])
                    l+=1
                ans+=(r-l+1)
            return ans
        return atmostK(k) - atmostK(k-1)
