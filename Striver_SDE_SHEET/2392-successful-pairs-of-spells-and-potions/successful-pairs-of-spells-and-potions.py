class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        N = len(potions)
        ans = list()
        potions.sort()
        for spell in spells:
            req = ceil(success/spell)
            ans.append(max(0,N-bisect_left(potions,req)))
        return ans