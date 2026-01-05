class Solution:
    def findMaxVal(self, N: int, restrictions: List[List[int]], diff: List[int]) -> int:
        temp = [inf]*N
        for idx,num in restrictions:
            temp[idx]=num
        
        for i in range(N-2,-1,-1):
            temp[i] = min(temp[i],temp[i+1]+diff[i])
        temp[0] = 0
        for i in range(N):
            temp[i] = min(temp[i],temp[i-1]+diff[i-1])
        return max(temp)