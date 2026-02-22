class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        '''
        * lcm of two numbers is always greater than or equal two the larger among the two
        * thus numbers > threshold will be single components
        '''
        N = len(nums)
        size = [1]*(threshold+1)
        parent = [u for u in range(threshold+1)]

        def find(u):
            while u!=parent[u]:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return parent[u]
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

        for u in nums:
            if u>threshold: 
                continue
            temp = u
            while temp<=threshold:
                union(u,temp)
                temp+=u
        vis = set()
        for u in nums:
            if u>threshold: 
                vis.add(u)
                continue
            p = find(u)
            vis.add(p)
        return len(vis)