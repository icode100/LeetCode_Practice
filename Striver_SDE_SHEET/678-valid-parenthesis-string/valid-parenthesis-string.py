class Solution:
    def checkValidString(self, s: str) -> bool:
        min,max = 0,0
        for c in s:
            if c=='(': 
                min+=1
                max+=1
            elif c==')':
                min-=1
                max-=1
            else:
                min-=1
                max+=1
            if max<0: return False
            if min<0: min=0
        if 0 in range(min,max+1): return True
        return False