class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        '''
        * sieve for finding primes
        * if the number is even then number//2 should be prime then sum = number + number//2 +2 +1
        * if number is odd find the least prime divisible by number if number%prime==0 then sum = number+prime+(1+number//prime)
        '''

        def sieve(N):
            isprime = [True]*(N+1)
            isprime[0] = isprime[1] = False
            p = 2
            while p*p<=N:
                if isprime[p]:
                    for i in range(p*p, N+1, p):
                        isprime[i] = False
                p+=1
            return [i for i in range(2,N+1) if isprime[i]]

        primes = set(sieve(100000))
        ans = 0

        for num in nums:
            root = round(num ** (1/3))
            if root**3 == num and (root in primes):
                ans += (1 + root + root*root + num)
            elif num & 1:
                p = 2
                while p*p <= num:
                    if num%p==0 and (num//p != p) and (p in primes) and (num//p in primes):
                        ans+=(p+1+(num//p)+num)
                        break
                    p+=1
            else:
                second = num>>1
                if (second!=2) and (second in primes):
                    ans+=(3+num+second)
            
        return ans


