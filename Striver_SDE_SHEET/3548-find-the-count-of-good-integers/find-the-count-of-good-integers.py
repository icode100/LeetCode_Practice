factorial = [1]
for i in range(1,11):
    factorial.append(factorial[-1]*i)

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        '''
        * generating all the palindromes of n digits that are divisible by k
        * finding all the permutations of the digit 
        * storing the sorted string of the number on visited set
        '''
        hashset = set()
        start = pow(10,(n-1)>>1)
        end = (start*10)-1
        for integer in range(start,end+1):
            string = str(integer)
            number = string+string[::-1][n&1:]
            if int(number)%k==0:
                hashset.add(''.join(sorted(number)))
        
        ans = 0
        for s in hashset:
            counter = Counter(s)
            total = factorial[n-1]*(n-counter['0'])
            for x in counter.values(): total//=factorial[x]
            ans+=total
            
        return ans
        

