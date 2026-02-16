class SegmentTree:
    def __init__(self, arr, operation, default):
        """
        arr: input array
        operation: lambda function (e.g. max, min)
        default: identity element (e.g. -inf for max, +inf for min)
        """
        self.n = len(arr)
        self.op = operation
        self.default = default
        
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        
        self.tree = [default] * (2 * self.size)
        
        # Build
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.op(
                self.tree[2 * i],
                self.tree[2 * i + 1]
            )

    def update(self, index, value):
        """Point update: arr[index] = value"""
        pos = self.size + index
        self.tree[pos] = value
        
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.op(
                self.tree[2 * pos],
                self.tree[2 * pos + 1]
            )
            pos //= 2

    def query(self, left, right):
        """
        Range query on [left, right]
        """
        left += self.size
        right += self.size
        
        res_left = self.default
        res_right = self.default
        
        while left <= right:
            if left % 2 == 1:
                res_left = self.op(res_left, self.tree[left])
                left += 1
            
            if right % 2 == 0:
                res_right = self.op(self.tree[right], res_right)
                right -= 1
            
            left //= 2
            right //= 2
        
        return self.op(res_left, res_right)


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        maxq,minq = deque(),deque()
        result = 0
        l = 0
        for r in range(N):
            while maxq and nums[maxq[-1]]<=nums[r]:
                maxq.pop()
            maxq.append(r)

            while minq and nums[minq[-1]]>=nums[r]:
                minq.pop()
            minq.append(r)

            while l<=r and (r-l+1)*(nums[maxq[0]]-nums[minq[0]])>k:
                if maxq and maxq[0]==l:
                    maxq.popleft()
                if minq and minq[0]==l:
                    minq.popleft()
                l+=1
            result+=(r-l+1)
        return result
            