class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        prev = 0
        ans = 0
        i = 1
        while i<n:
            maxt = neededTime[prev]
            tott = neededTime[prev]
            while i<n and colors[i]==colors[prev]:
                tott+=neededTime[i]
                maxt = max(maxt,neededTime[i])
                i+=1
            ans+=(tott-maxt)
            prev = i
            i+=1
        return ans


            
