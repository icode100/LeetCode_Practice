class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        N = len(s)
        c0,c1 = 0,0
        for si,ti in list(zip(s,t)):
            if si=='0' and ti=='1': c0+=1
            elif si=='1' and ti=='0': c1+=1
        flip = (c1+c0)*flipCost
        swap = min(c0,c1)*swapCost + abs(c0-c1)*flipCost
        cross = min(c0,c1)*swapCost + (abs(c0-c1)//2)*(crossCost+swapCost) + (abs(c0-c1)%2)*flipCost

        return min(flip,swap,cross)
        
        


        