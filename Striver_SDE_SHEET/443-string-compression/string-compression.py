class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 0
        updator = 0
        length = 0
        while counter<len(chars):
            top = chars[counter]
            count = 0
            while counter<len(chars) and chars[counter]==top:
                count+=1
                counter+=1
            temp = top+str(count) if count!=1 else top
            for c in temp:
                chars[updator] = c
                updator+=1
                length+=1
        return length