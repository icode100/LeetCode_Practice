class Solution:
    def canIWin(self, n: int, target: int) -> bool:
        if (n*(n+1))//2 < target: return False
        if target<n: return True
        @cache
        def recursion(mask,current):
            # if current<=0: return True
            ans = False
            for i in range(1,n+1):
                if mask&(1<<i) == 0:
                    if i>=current: return True
                    ans = ans or not recursion(mask|(1<<i), current-i)
            return ans
        ans = recursion(0,target)
        return ans