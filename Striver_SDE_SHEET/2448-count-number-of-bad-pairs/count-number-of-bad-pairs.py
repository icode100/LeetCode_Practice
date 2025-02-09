class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        ans = 0
        for i,num in enumerate(nums):
            ans+=(i-hashmap[num-i])
            hashmap[num-i]+=1
        return ans