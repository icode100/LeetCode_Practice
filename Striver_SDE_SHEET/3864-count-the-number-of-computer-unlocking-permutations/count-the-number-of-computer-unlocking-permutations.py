class Solution:
    def __init__(self):
        self.mod = int(1e9+7)
    def countPermutations(self, complexity: List[int]) -> int:
        if min(complexity)!=complexity[0]: return 0
        if complexity.count(complexity[0])>1: return 0

        N = len(complexity)
        
        return factorial(N-1)%self.mod