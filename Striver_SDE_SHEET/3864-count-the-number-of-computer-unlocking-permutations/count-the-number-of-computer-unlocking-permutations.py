class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        return 0 if (min(complexity)!=complexity[0]) or (complexity.count(complexity[0])>1) else factorial(len(complexity)-1)%int(1e9+7)