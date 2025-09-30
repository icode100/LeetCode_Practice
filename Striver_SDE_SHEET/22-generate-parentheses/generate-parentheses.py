class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = list()
        @cache
        def recursion(current):
            if len(current)==(n*2):
                print(current)
                ans.append(current)
                return 
            for i in range(len(current)+1):
                recursion(current[:i]+'()'+current[i:])
        recursion("()")
        return ans
            