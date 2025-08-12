class Solution:
    def findTheLongestSubstring(self, string: str) -> int:
        hashmap = {0:-1}
        vowels = 'aeiou'
        mask = 0
        ans = 0
        for i,c in enumerate(string):
            if c in vowels:mask^=(1<<vowels.index(c))
            if mask in hashmap: ans = max(ans,i-hashmap[mask])
            else: hashmap[mask] = i
        return ans



