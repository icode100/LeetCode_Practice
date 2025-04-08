class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        total = sum(cardPoints)
        current = sum(cardPoints[:N-k])
        ans = current
        for i in range(N-k,N):
            current+=(cardPoints[i]-cardPoints[i-N+k])
            ans = min(ans,current)
        return total-ans


