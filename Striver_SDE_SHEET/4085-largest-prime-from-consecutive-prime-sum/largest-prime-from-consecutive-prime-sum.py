class Solution:
    def sieve(self,limit:int)->List[int]:
        primeMap:List[bool] = [False]*(limit+1)
        i:int = 2

        while i*i<=limit:

            if primeMap[i]==False:
                j:int = i*i

                while j<=limit:
                    primeMap[j] = True
                    j+=i
            i+=1

        return [i for i in range(2,limit+1) if not primeMap[i]]

    def largestPrime(self, n: int) -> int:
        primes:List[int] = self.sieve(n)
        primeSet:Set[int] = set(primes)
        ans:int = 0
        primes = list(accumulate(primes))

        for num in primes:
            if num in primeSet:
                ans = max(ans,num)
        
        return ans


        
        