class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        '''
        * So lets mask be defining the state of the vowel count parity in the current traversed prefix 
        * so mask is of 5 bits
        * if we have got the mask mask before and the mask not zero it means we need to remove the prefix till the index at which the current prefix mask have occurred before
        * to remove the minimum prefix so as to maximize the subarray length we remove the index of FIRST occurence of the mask
        * "eleet"
        * i = 0: mask = 0b00010 the current mask did not occur before so length is 0 -> ""
        * i = 1: mask = 0b00010 the current mask first occured at i=0, so length is 1-0 = 1 -> "l"
        * i = 2: mask = 0b00000 the current mask first occured at i=-1, so length is 2-(-1) = 3 -> "ele"
        * i = 3: mask = 0b00010 the current mask first occured at i=0, so length is 3-0 = 3 -> "lee"
        * i = 4: mask = 0b00010 the current mask first occured at i=0, so the length is 4-0 = 4 -> "leet"
        '''
        hashmap = {0: -1}
        mapper = {'a':1,'e':2,'i':3,'o':4,'u':5}
        mask = 0
        ans = 0
        N = len(s)
        for i in range(N):
            if s[i] in mapper: mask ^= (1<<mapper[s[i]])
            if mask in hashmap:
                ans = max(ans,i-hashmap[mask])
            else:
                hashmap[mask] = i
        return ans
