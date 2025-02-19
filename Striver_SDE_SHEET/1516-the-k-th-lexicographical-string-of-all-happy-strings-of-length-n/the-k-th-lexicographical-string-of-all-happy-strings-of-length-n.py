class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k>3*(1<<(n-1)): return ""
        stack = []
        while len(stack)<n and k>0:
            for c in ["a","b","c"]:
                if not stack or stack[-1]!=c:
                    stack.append(c)
                    val = (1<<(n-len(stack)))
                    if val>=k: break
                    else: 
                        stack.pop()
                        k-=val
        return ''.join(stack)



            
