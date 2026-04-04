class Solution:
    def countGoodSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        prev_one = [-1] * 31
        next_one = [n] * 31
        
        L, R = [0] * n, [n - 1] * n
        
        for i in range(n):
            for bit in range(31):
                if (nums[i] & (1 << bit)) == 0:
                    L[i] = max(L[i], prev_one[bit] + 1)
                else:
                    prev_one[bit] = i
                    
        for i in range(n - 1, -1, -1):
            for bit in range(31):
                if (nums[i] & (1 << bit)) == 0:
                    R[i] = min(R[i], next_one[bit] - 1)
                else:
                    next_one[bit] = i
                    
        ans = 0
        last_idx = {}
        
        for i in range(n):
            l, r = L[i], R[i]
            
            if nums[i] in last_idx:
                l = max(l, last_idx[nums[i]] + 1)
            last_idx[nums[i]] = i
            
            ans += (i - l + 1) * (r - i + 1)
            
        return ans