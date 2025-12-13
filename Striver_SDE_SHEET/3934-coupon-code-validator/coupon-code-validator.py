class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        N:int = len(code)
        busMapper:DefaultDict[str,SortedList[str]] = defaultdict(lambda:SortedList())
        order:List[str] =  ["electronics","grocery","pharmacy", "restaurant"]
        ans:List[str] = list()

        def codeCheck(code:str):
            for s in code: 
                if not s.isalnum() and s!='_': return False
            return True

        for i in range(N):
            i:int

            if code[i]!="" and codeCheck(code[i]) and businessLine[i] in order and isActive[i]:
                busMapper[businessLine[i]].add(code[i])
        
        for business in order:
            business:str

            ans.extend(list(busMapper[business]))
        
        return ans



