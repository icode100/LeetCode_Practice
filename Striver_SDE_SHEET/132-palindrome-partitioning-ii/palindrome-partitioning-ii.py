class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def recursion(string):
            if string==string[::-1]: 
                return 0
            if len(string)<=1:
                return 0
            ans = int(1e9)
            for i in range(1,len(string)):
                temp = string[:i]
                if temp==temp[::-1]:
                    ans = min(ans,1+recursion(string[i:]))
            return ans
        return recursion(s)

