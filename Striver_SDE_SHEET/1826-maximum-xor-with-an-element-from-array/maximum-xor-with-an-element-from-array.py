class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = dict()
        def insert(num):
            depth = trie
            mask = 1<<32
            while mask:
                val = num&mask if num&mask==0 else 1
                # print(val)
                if val in depth:
                    depth = depth[val]
                else:
                    depth[val] = dict()
                    depth = depth[val]
                mask = mask>>1
        def getmax(x):
            mask = 1<<32
            depth = trie
            num = 0
            while mask:
                val = x&mask if x&mask==0 else 1
                need = 1-val
                if need in depth:
                    depth = depth[need]
                    num = (num<<1)|1
                elif val in depth:
                    num = (num<<1) | 0
                    # print(x,mask,x&mask)
                    depth = depth[val]
                else: return -1
                mask = mask>>1
            return num
        hashmap = dict()
        nums.sort()
        # print(queries,nums)
        i = 0
        for x,m in sorted(queries,key = lambda x:x[1]):
            while i<len(nums) and nums[i]<=m:
                # print("hi")
                insert(nums[i])
                i+=1
            # print(trie)
            hashmap[(x,m)] = getmax(x) 
        # print(hashmap)
        return [hashmap[(x,m)] for x,m in queries]
                            
        