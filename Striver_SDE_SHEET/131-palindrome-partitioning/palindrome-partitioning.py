class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = list()
        def recursion(index,stack):
            if index>=len(s):
                ans.append(stack.copy())
                return
            for i in range(index,len(s)):
                if s[index:i+1]=="".join(reversed(s[index:i+1])): 
                    recursion(i+1,stack+[s[index:i+1]])
        recursion(0,[])
        return ans                    

            