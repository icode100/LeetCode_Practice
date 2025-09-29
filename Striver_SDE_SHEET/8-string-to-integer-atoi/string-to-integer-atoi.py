class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        print(s)
        ans = '0'
        sign = 1
        for i,c in enumerate(s):
            if i==0 and c in '+-': 
                sign = -1 if c=="-" else 1
            elif c in '1234567890': ans+=c
            else: 
                print(c)
                break
        INT_MAX,INT_MIN = ((1<<31)-1), -(1<<31)
        val = int(ans)*sign
        return val if INT_MIN<=val<=INT_MAX else (INT_MIN if val<0 else INT_MAX)