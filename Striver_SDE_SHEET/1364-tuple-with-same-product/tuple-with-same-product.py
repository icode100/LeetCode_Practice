class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                hashmap[nums[i]*nums[j]]+=1
        ans = 0
        for val,f in hashmap.items():
            ans+=((f*(f-1))>>1)*8
        return ans
