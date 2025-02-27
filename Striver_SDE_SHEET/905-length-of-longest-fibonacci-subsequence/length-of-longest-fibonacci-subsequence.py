class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashset = set()
        numset = set(arr)
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                first,second = arr[i],arr[j]
                if (first,second) in hashset: continue
                current = 1
                while second in numset:
                    hashset.add((first,second))
                    third = first+second
                    first = second
                    second = third
                    current+=1
                ans = max(ans,current)
        return ans if ans>2 else 0
