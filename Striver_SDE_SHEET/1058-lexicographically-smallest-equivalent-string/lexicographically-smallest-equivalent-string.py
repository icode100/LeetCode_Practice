alpha = 'abcdefghijklmnopqrstuvwxyz'
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {x:x for x in alpha}
        def find(x):
            if parent[x]==x: return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(u,v):
            ultu,ultv = find(u),find(v)
            if ultu==ultv: return
            if ultu<ultv: parent[ultv] = ultu
            else: parent[ultu] = ultv
        for u,v in zip(list(s1),list(s2)):
            union(u,v)

        ans = ""
        for s in baseStr: ans+=find(s)
        return ans



