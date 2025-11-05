class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        N = len(nums)>>1
        dp_left,dp_right = {i:list() for i in range(N+1)},{i:list() for i in range(N+1)}
        for mask in range(1<<N):
            count,leftsum,rightsum = 0,0,0
            for i in range(N):
                if mask&(1<<i):
                    count+=1
                    leftsum+=nums[i]
                    rightsum+=nums[i+N]
            dp_left[count].append(leftsum)
            dp_right[count].append(rightsum)
        for i in range(N+1):
            dp_right[i].sort()
        target = total/2
        ans = inf
        for cnt in range(N+1):
            for num in dp_left[cnt]:
                need = target-num
                idx = bisect_left(dp_right[N-cnt],need)
                if idx<len(dp_right[N-cnt]):
                    ans = min(ans,abs(total-2*(num+dp_right[N-cnt][idx])))
                if idx>0: 
                    ans = min(ans,abs(total-2*(num+dp_right[N-cnt][idx-1])))
        return ans