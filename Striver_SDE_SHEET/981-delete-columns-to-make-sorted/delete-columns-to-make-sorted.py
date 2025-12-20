class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns:List[str] = map(lambda x: "".join(x), list(zip(*strs)))
        count:int = 0

        for col in columns:
            if col!=''.join(sorted(list(col))): 
                count+=1
            
        return count