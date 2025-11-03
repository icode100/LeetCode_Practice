class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = int(1e9+7)
        nums = list(map(int,list(num)))
        counter = [0]*10
        for i in nums: counter[i]+=1
        #if the sum of numbers is odd we cannot do permutations 
        if sum(nums)&1: return 0
        target = sum(nums)>>1
        N = len(nums)
        '''
        we need prefix sum so that if we can compute the following:
        * we have completed the filling till i-1 digits and are in state of filling i digits then the number of remaining places to be filled being missing = N - sum(cnt[i] for i in range(i))
        * hence the number of even places to be filled shall be missing - oddMissing
        '''
        prefix_sum = [0]*11
        for i in range(1, 11):
            prefix_sum[i] = prefix_sum[i-1] + counter[i-1]

        @cache
        def recursion(num,current,oddMissing):
            missing = N - prefix_sum[num]
            if oddMissing<0 or missing<oddMissing or current>target: return 0
            if num>9: return int(current==target and oddMissing==0)
            evenMissing = missing-oddMissing
            ans = 0
            lo = max(0, counter[num] - evenMissing)
            hi = min(counter[num], oddMissing)
            for i in range(lo,hi+1):
                ways = comb(oddMissing,i)*comb(evenMissing,counter[num]-i)%MOD
                ans+=ways*recursion(num+1,current+i*num, oddMissing-i)
            return ans%MOD
        return recursion(0,0,(N+1)//2)
                