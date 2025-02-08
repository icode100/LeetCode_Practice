class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * (n + 1)

        # Compute gaps
        gaps[0] = startTime[0]  
        gaps[n] = eventTime - endTime[-1]  
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]

        # Sliding window of size k + 1
        window = sum(gaps[:k + 1])
        ans = window
        for i in range(k + 1, n + 1):
            window += gaps[i] - gaps[i - (k + 1)]
            ans = max(ans, window)

        return ans