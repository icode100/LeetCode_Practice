class Solution:
    def kSmallestPairs(self, A: List[int], B: List[int], k: int) -> List[List[int]]:
        N,M = len(A), len(B)
        heap = [[A[0]+B[i], [A[0],B[i]], 0] for i in range(M)]
        heapify(heap)
        ans = list()
        while k:
            sum,pair,index = heappop(heap)
            ans.append(pair)
            k-=1
            if index+1<N:
                sum = A[index+1]+pair[1]
                heappush(heap, [sum, [A[index+1], pair[1]], index+1])
        
        return ans

