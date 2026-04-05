class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        '''
        * for odd length we can have n/2 + 1 peaks thats the max by making all theodd indices peaks
        * for even length we use dp because we can skip one extra position to reduce costs
        like in this example [31,34,20,6,15,19] and we can skip extra only once for the sake of keeping the count of peaks consistent and minimizing the cost
        '''
        N = len(nums)
        cost = [0]*N
        for i in range(1,N-1):
            cost[i] = max(cost[i],max(nums[i-1],nums[i+1])-nums[i]+1)
        if N&1:
            return sum(cost[i] for i in range(1,N-1,2))
            
        @cache
        def recursion(i,isskip):
            if i>=N-1:
                return 0
            c = cost[i]
            if isskip:
                return c+recursion(i+2,True)
            return min(
                c+recursion(i+2,False),
                c+recursion(i+3,True)
            )
        return min(recursion(1,False), recursion(2, True))
