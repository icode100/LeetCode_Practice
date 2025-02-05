class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        hashmap = [0]*(n+1)
        for i,j in requests:
            hashmap[i]+=1
            hashmap[j+1]-=1
        for i in range(1,len(hashmap)): hashmap[i]+=hashmap[i-1]
        hashmap = hashmap[:-1]
        trav = list(zip(sorted(hashmap),sorted(nums)))
        ans = 0
        for i in range(len(trav)):
            f,n = trav[i]
            ans += (f*n)
        return ans%int(1e9+7)