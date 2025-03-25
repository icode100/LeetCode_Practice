class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counter = Counter(hand)
        for x in hand:
            if x not in counter: continue
            for diff in range(groupSize):
                if x+diff not in counter: return False
                counter[x+diff]-=1
                if counter[x+diff]==0: counter.pop(x+diff)
        return True 
            
                
        



