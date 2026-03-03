class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(k+1)]
        best = [0]*(k+1)
        best_val = [None]*(k+1)
        second_best = [0]*(k+1)
        for num in nums:
            for t in range(k,-1,-1):
                dp[t][num]+=1

                change = 0
                if t>0:
                    if best_val[t-1]!=num:
                        change = best[t-1]+1
                    else:
                        change = second_best[t-1]+1
                dp[t][num] = max(
                    dp[t][num],
                    change
                )
                
                if dp[t][num]>best[t]:
                    if num!=best_val[t]:
                        second_best[t] = best[t]
                    best[t] =  dp[t][num]
                    best_val[t] = num
                elif num!=best_val[t]:
                    second_best[t] = max(second_best[t],dp[t][num])
        return max(best)
