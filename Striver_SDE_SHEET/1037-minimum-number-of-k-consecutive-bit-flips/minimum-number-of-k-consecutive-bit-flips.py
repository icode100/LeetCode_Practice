class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        count = 0
        for i in range(n):
            while q and q[0]<i-k+1: q.popleft()
            if nums[i]==0:
                if len(q)&1: continue
                else: 
                    if i+k>n: return -1
                    count+=1
                    q.append(i)
            if nums[i]==1:
                if len(q)&1:
                    if i+k>n: return -1
                    count+=1 
                    q.append(i)
                else: continue
        return count
            


            