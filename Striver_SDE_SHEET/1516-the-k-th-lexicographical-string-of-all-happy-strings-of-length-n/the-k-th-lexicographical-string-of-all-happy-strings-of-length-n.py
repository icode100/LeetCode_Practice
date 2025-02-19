class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        no_strings_attached = ['a','b','c']
        stack = []
        ans = ""
        k = k
        def recursion(index):
            nonlocal ans,k
            if index==n:
                k-=1
                if k==0:
                    print(stack)
                    ans = ''.join(stack)
                return
            for i in no_strings_attached:
                if not stack or i!=stack[-1]: 
                    stack.append(i)
                    recursion(index+1)
                    stack.pop()
            return 
        recursion(0)
        return ans

            
