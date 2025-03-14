class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        line = [0]*n
        for s,e in queries:
            line[s]+=1
            if e+1<n: line[e+1]-=1
        current = 0
        for i in range(n):
            current+=line[i]
            if current<nums[i]: return False
        return True
