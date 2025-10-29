class Solution:
    def findTheLongestSubstring(self, string: str) -> int:
        hashmap = defaultdict()
        mask = 0
        ans = 0
        for i,c in enumerate(string):
            if c in "aeiou": mask^=(1<<ord(c))
            if mask == 0: ans = max(ans,i+1)
            elif mask in hashmap: ans = max(ans,i-hashmap[mask])
            else : hashmap[mask] = i
        return ans



