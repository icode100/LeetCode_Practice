class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        M = len(queries)
        queries.sort()
        j = 0
        delta = [0]*(N+1)
        heap = list()
        operations = 0
        for i,num in enumerate(nums):
            operations -= delta[i]
            while j<M and len(queries) and queries[j][0]==i:
                heappush(heap,-queries[j][1])
                j+=1
            while operations<num and heap and -heap[0]>=i:
                operations+=1
                delta[-heappop(heap)+1]+=1
            if operations<num: return -1
        print(delta)
        return len(heap)

