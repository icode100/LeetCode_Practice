class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hashmap = dict()
        n = len(accounts)
        parent = [v for v in range(n)] 
        size = [1 for v in range(n)] 
        def find(node): 
            if node==parent[node]: return node 
            parent[node] = find(parent[node]) 
            return parent[node]
        def union(u,v): 
            ultu,ultv = find(u),find(v) 
            if ultu==ultv: return False 
            if size[ultu]<size[ultv]: 
                parent[ultu] = ultv 
                size[ultv]+=size[ultu] 
            else: 
                parent[ultv] = ultu 
                size[ultu]+=size[ultv] 
            return True
        for i in range(n):
            for email in accounts[i][1:]:
                if email not in hashmap: hashmap[email] = i
                else:
                    union(hashmap[email],i)
        mergedacc = defaultdict(list)
        for email in sorted(hashmap.keys()):
            place = find(hashmap[email])
            mergedacc[place].append(email)
        return [[accounts[place][0]]+mergedacc[place] for place in sorted(mergedacc.keys())]