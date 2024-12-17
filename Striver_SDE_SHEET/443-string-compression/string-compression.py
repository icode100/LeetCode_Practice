class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        n = len(chars)
        count = 0
        if len(chars)<2:
            return len(chars)
        while right<n:
            c = chars[right]
            while right<n and chars[right] == c:
                count+=1
                right+=1
            chars[left] = c
            left+=1
            if count>1:
                for char in str(count):
                    chars[left] = char
                    left+=1
            count=0
        # print(left,right)
        # print(chars)
        # chars[left] = str(count)
        # left+=1
        return left



