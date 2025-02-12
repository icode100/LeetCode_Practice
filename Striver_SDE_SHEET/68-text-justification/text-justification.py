class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        current = 0
        n = len(words)
        q = deque()
        i = 0
        ans = list()
        while i<n:
            current += len(words[i])
            if current+len(q)<=maxWidth:
                q.append(words[i])
            else:
                efflen,effnum = current-len(words[i]),len(q)
                reqlen = efflen+effnum-1
                extra = maxWidth-reqlen
                res = ""
                if effnum-1==0: 
                    spaces,uneven = extra,0
                    res+=q.popleft()+(" "*spaces)
                else: 
                    spaces,uneven = divmod(extra,effnum-1)
                    while q:
                        string = q.popleft()
                        res+=string + (" " if len(q)>0 else "")
                        if spaces: res = res+ (" "*spaces if len(q)>0 else "")
                        if uneven>0 and len(q)>0:
                            res+=' '
                            uneven-=1
                ans.append(res)
                q.append(words[i])
                current = len(words[i])
            i+=1
        efflen,effnum = current,len(q)
        reqlen = efflen+effnum-1
        extra = maxWidth-reqlen
        res = ""
        while q:
            res+= (q.popleft() + (" " if len(q)>0 else ""))
        res+=' '*extra
        ans.append(res)
        return ans



            
