class Solution:
    def __init__(self):
        self.mod = int(1e9+7)

    def specialTriplets(self, nums: List[int]) -> int:
        N:int = len(nums)
        mapper: DefaultDict[List[int]] = defaultdict(list)
        ans:int = 0

        for i,num in enumerate(nums):
            mapper[num].append(i)

        for j in range(N):
            j:int

            tar:int = (nums[j]*2)
            if tar not in mapper: continue
            tarArr:List[int] = mapper[tar]
            M:int = len(tarArr)

            idx:int = bisect_left(tarArr,j)
            if idx==M or idx==0 or (idx==M-1 and tarArr[idx]==j) or (idx==0 and tarArr[idx]==j): continue
            if tarArr[idx]==j:
                ans = (ans+ (idx*(M-idx-1))) % self.mod
            else: 
                ans = (ans + (idx*(M-idx))) % self.mod
        
            # print(j,idx, tarArr)
        return ans





