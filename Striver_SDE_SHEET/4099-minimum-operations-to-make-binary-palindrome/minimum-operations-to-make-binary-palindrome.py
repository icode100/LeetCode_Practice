class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        
        def isPalindrome(num):
            if num < 2:
                return True

            left = num.bit_length() - 1
            right = 0

            while left > right:
                if ((num >> left) & 1) != ((num >> right) & 1):
                    return False
                left -= 1
                right += 1

            return True

        palindromes = [0,1]
        for i in range(3,5000):
            if isPalindrome(i): 
                palindromes.append(i)

        print(palindromes)

        ans = list()
        for num in nums:
            idx = bisect_left(palindromes,num)
            if idx==len(palindromes):
                ans.append(num-palindromes[-1])
            elif palindromes[idx]==num: ans.append(0)
            elif idx==0:
                ans.append(palindromes[0]-num)
            else:
                ans.append(min(abs(palindromes[idx]-num),abs(palindromes[idx-1]-num)))

        return ans

        

    