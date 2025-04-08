class Solution:
    def partitionString(self, s: str) -> int:
        mask = 0
        count = 0
        for i,c in enumerate(s):
            if (1<<(ord(c)-ord('a')))&mask==0: mask |= (1<<(ord(c)-ord('a')))
            else: 
                mask = 1<<(ord(c)-ord('a'))
                count+=1
        return count+1