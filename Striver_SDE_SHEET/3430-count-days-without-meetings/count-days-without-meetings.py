class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        line = SortedDict()
        for s,e in meetings:
            line[s] = line.get(s,0)+1
            line[e+1] = line.get(e+1,0)-1
        current,count = 0,0
        previ = 1
        for k in line:
            if current==0:
                count+=k-previ
            current+=line[k]
            if current==0: 
                previ = k
        return count+days-previ+1
            
         