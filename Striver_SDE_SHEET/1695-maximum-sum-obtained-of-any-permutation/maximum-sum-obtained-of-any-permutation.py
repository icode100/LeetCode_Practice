class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        counter = [0]*N
        for start,end in requests:
            counter[start] +=1
            if end+1<N: counter[end+1] -=1
        for i in range(1,N): counter[i]+=counter[i-1]
        return sum(n*c for n,c in list(zip(sorted(counter),sorted(nums)))) % int(1e9+7)

        
