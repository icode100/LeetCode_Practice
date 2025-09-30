INT_MAX,INT_MIN = ((1<<31)-1), -(1<<31)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:return 0
        sign = 1
        i = 0
        if s[0] in '+-':
            sign=-1 if s[0]=='-' else 1
            i+=1
        def recursion(i,current):
            if i>=len(s) or not s[i].isdigit():
                return sign*int(current)
            current = current*10 + int(s[i])
            if sign*current>INT_MAX: return INT_MAX
            if sign*current<INT_MIN: return INT_MIN
            return recursion(i+1,current)
        current = 0
        return recursion(i,current)