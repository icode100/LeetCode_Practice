class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stock = defaultdict(int)
        for bill in bills:
            if bill==5: stock[5]+=1
            elif bill==10:
                if stock[5]:
                    stock[5]-=1
                    stock[10]+=1
                else: return False
            else:
                if stock[10]>0 and stock[5]>0: 
                    stock[10]-=1
                    stock[5]-=1
                    stock[20]+=1
                elif stock[5]>=3: 
                    stock[5]-=3
                    stock[20]+=1
                else: return False
        return True