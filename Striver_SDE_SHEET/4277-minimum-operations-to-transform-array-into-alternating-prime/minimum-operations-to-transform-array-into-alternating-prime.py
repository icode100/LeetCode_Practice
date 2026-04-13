class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def sieve(n):
            primes = [True]*n
            primes[0]=primes[1]=False
            p = 2
            while p*p<=n:
                if primes[p]:
                    for i in range(p*p,n+1,p):
                        primes[i] = False
                p+=1
            return [i for i in range(n) if primes[i]]
        
        primes = sieve(int(1e5+19))
        primeset = set(primes)
        count = 0

        for i in range(len(nums)):
            if (i&1)==0:
                if nums[i] in primeset:
                    continue
                else:
                    idx = bisect_left(primes,nums[i])
                    count+=primes[idx]-nums[i]
            else:
                if nums[i] not in primeset:
                    continue
                else:
                    if nums[i]==2:
                        count+=2
                    else:
                        count+=1
        return count


