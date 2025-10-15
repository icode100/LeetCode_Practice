class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = SortedDict()
        for i in hand:
            counter[i] = counter.get(i,0)+1
        
        while counter:
            start = counter.peekitem(0)[0]
            for i in range(groupSize):
                if start+i in counter:
                    counter[start+i]-=1
                    if counter[start+i]==0: counter.pop(start+i)
                else: return False
        return True
