class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i,num in enumerate(nums):
            hashmap[num-i]+=1
        ans = 0
        for key,val in hashmap.items():
            ans+=(((val)*(val-1))>>1)
        return ((len(nums)*(len(nums)-1))>>1)-ans
        