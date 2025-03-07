class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def recursion(expression):
            if len(expression)==1: return [int(expression)]
            if len(expression)==2 and expression[0].isdigit(): return [int(expression)]
            ans = list()
            for i,k in enumerate(expression):
                if k.isdigit(): continue
                left = recursion(expression[:i])
                right = recursion(expression[i+1:])
                for l in left:
                    for ri in right:
                        if k=='+': ans.append(l+ri)
                        elif k=='-': ans.append(l-ri)
                        else: ans.append(l*ri)
            return ans
        return recursion(expression)

            
