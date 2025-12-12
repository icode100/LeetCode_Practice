class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans:List[int] = [0]*numberOfUsers
        events.sort(key=lambda x: (int(x[1]), x[0] != 'OFFLINE'))
        current = 0
        offlineMap:Dict[int,int] = {i:-1 for i in range(numberOfUsers)}
        for event in events:
            event:List[str]

            msgType, timeStamp, mainString = event
            msgType:str
            timeStamp:str
            mainString:str
            timeInt:int = int(timeStamp)

            if msgType=='MESSAGE':
                if mainString=="ALL":
                    for i in range(numberOfUsers): ans[i]+=1
                elif mainString=="HERE":
                    for i in range(numberOfUsers): 
                        if timeInt>=offlineMap[i]: ans[i]+=1
                else:
                    convert:Callable[[str], int] = lambda x: int(x[2:])
                    users:List[int] = list(map(convert,mainString.strip().split()))
                    for user in users:
                        ans[user]+=1
            else:
                user:int = int(mainString)
                offlineMap[user] = timeInt+60
        
        return ans
                

