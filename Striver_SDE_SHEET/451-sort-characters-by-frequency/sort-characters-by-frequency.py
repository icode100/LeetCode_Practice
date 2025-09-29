class Solution:
    def frequencySort(self, s: str) -> str:
        temp = list(Counter(s).items())
        temp.sort(key = lambda x: (-x[1],x[0]))
        res = ""
        for c,f in temp: res+=c*f
        return res