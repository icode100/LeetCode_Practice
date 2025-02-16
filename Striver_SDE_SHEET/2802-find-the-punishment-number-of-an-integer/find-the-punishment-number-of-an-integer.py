def recursion(i,num,target):
    if target==0:
        if i==len(num): return True
    if i>len(num): return False
    current = ""
    ans = False
    for j in range(i,len(num)):
        current+=num[j]
        if int(current)<=target:
            # print(i,num,target,current,target-int(current),j+1)
            ans = ans or recursion(j+1,num,target-int(current))
    return ans
square = list()
print(recursion(0,'100',10))
for i in range(1,1001): 
    num = i*i
    if recursion(0,str(num),i): square.append(num)

# print(square)
class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        check = n*n
        for i in square: 
            # print(i)
            if i<=check: ans+=i
        return ans