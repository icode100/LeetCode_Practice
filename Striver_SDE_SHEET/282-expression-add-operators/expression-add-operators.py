class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        strings = list()
        def recursion(index,ans,prev,current):
            if index==len(num):
                if current==target: strings.append(ans)
                return
            for i in range(index,len(num)):
                integer = int(num[index:i+1])
                if len(str(integer))!=len(num[index:i+1]): break
                if index==0:
                    recursion(i+1,str(integer),integer,integer)
                else:
                    recursion(i+1,ans+'+'+str(integer),integer,current+integer)
                    recursion(i+1,ans+'-'+str(integer),-integer,current-integer)
                    recursion(i+1,ans+'*'+str(integer),prev*integer,current-prev+(prev*integer))
        recursion(0,"",0,0)
        return strings
