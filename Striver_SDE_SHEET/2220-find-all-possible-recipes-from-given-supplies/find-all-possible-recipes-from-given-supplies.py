class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        needed = defaultdict(list)
        vis = {i: True for i in supplies}
        supplies = set(supplies)
        for i,rec in enumerate(recipes):
            needed[rec] = ingredients[i]
        # print(needed)
        def dfs(node):
            if node in vis: return vis[node]
            if node not in needed and node not in supplies: return False
            vis[node] = False
            for req in needed[node]:
                # print(req)
                if not dfs(req):
                    return False
            vis[node] = True
            return True
        return [r for r in recipes if dfs(r)]
        

        