class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        count = 0
        l = 0
        for i,c in enumerate(chars):
            if c==prev: count+=1
            else:
                chars[l] = prev
                l+=1
                if count>1: 
                    for ch in str(count): 
                        chars[l] = ch
                        l+=1
                prev = c
                count = 1

        chars[l] = prev
        l+=1        
        if count>1: 
            for ch in str(count): 
                chars[l] = ch
                l+=1
        return l

