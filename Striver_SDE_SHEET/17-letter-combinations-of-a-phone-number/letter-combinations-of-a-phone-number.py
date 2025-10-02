class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans = list()
        def recursion(index,current):
            if index>=len(digits): 
                if current!="":ans.append(current)
                return
            for c in hashmap[digits[index]]:
                recursion(index+1,current+c)
        recursion(0,"")
        return ans
