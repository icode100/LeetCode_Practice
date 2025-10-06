class Solution:
    def countPrimes(self, n: int) -> int:
        def sieve(n):
            num = 2
            primes = set(range(2,n))
            for num in range(2,ceil(sqrt(n))):
                if num in primes:
                    for i in range(num*num,n,num):
                        if i in primes:
                            primes.remove(i)
            return len(primes)
        return sieve(n)
