class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = 0
        temp = k-1
        num1,parity1 = 0,1
        num2,parity2 = 1,0
        while temp:
            num1,num2 = (num1<<1),(num2<<1)
            num1,num2 = num1|parity1, num2|parity2
            parity1,parity2 = 1-parity1, 1-parity2
            temp-=1
        current = 0
        for i in range(k):
            current = current<<1
            current = current|colors[i]
        # print(current)
        # print((current<<1)&((1<<k)-1))
        if current==num1 or current==num2: ans+=1
        for left in range(1,n):
            current = (current<<1)&((1<<k)-1)
            current = current|colors[(left+k-1)%n]
            # print(current)
            if current==num1 or current==num2: ans+=1
        return ans



        

