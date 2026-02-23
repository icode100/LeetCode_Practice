class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        if 1 in nums: return False
        N = len(nums)
        M = max(nums)
        def sieve(N):
            primes = [i for i in range(N+1)]
            i = 2
            while i*i<=N:
                if primes[i] == i:
                    j = i*i
                    while j<=N:
                        primes[j] = i
                        j+=i
                i+=1
            return primes
        
        primes = sieve(M)

        parent = [i for i in range(M+1)]
        size = [1 for _ in range(M+1)]

        def find(u):
            if u==parent[u]: return u
            parent[u] = find(parent[u])
            return parent[u]
        def union(u,v):
            ultu,ultv = find(u),find(v)
            if ultu==ultv: return False
            if size[ultu]<size[ultv]:
                parent[ultu] = ultv
                size[ultv]+=size[ultu]
            else:
                parent[ultv] = ultu
                size[ultu]+=size[ultv]
            return True
        
        for i,num in enumerate(nums):
            temp = num
            while temp>1:
                union(primes[temp],num)
                temp//=primes[temp]

        parents = set()
        for num in nums:
            parents.add(find(num))
        return len(parents)==1
        
