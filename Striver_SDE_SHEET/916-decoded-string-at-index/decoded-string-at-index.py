class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for c in s: length = length+1 if not c.isdigit() else length*int(c)
        for c in reversed(s):
            k%=length
            if k==0 and not c.isdigit(): return c
            length = length-1 if not c.isdigit() else length//int(c)
        return ""