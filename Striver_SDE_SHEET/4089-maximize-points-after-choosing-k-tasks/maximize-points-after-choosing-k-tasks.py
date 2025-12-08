class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        N = len(technique1)

        difference = sorted([(technique1[i],technique2[i]) for i in range(N)],key = lambda x: x[0]-x[1],reverse = True)

        ans = 0
        for i in range(k):
            ans+=difference[i][0]
        
        for i in range(k,N):
            ans+=max(difference[i][0], difference[i][1])
        
        return ans
        
