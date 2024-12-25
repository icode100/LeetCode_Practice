class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counter = Counter(hand)
        ends = defaultdict(int)
        for i in hand:
            if counter[i]==0: continue
            for j in range(groupSize):
                if counter[i+j]!=0:
                    counter[i+j]-=1
                else: return False
        return True
                
        



