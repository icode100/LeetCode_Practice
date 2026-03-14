class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        idx = 1
        ans = ""
        while idx<n+1:
            count = 0
            for c in 'abc':
                if ans and c == ans[-1]: continue
                temp = (1<<(n-idx))
                count+=temp
                if count>=k:
                    ans+=c
                    k-=(count-temp)
                    break
            idx+=1
        return ans
