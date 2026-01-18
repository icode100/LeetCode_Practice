class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        N = len(nums)
        non_matched = [i for i in range(N) if nums[i]!=target[i]]

        counter = Counter()
        for i in non_matched: counter[nums[i]]+=1

        heap = list()
        for k,v in counter.items(): heappush(heap, (-v,k))

        count = len(non_matched)
        op = 0
        while heap and count>0:
            v,k = heappop(heap)
            count+=v
            op+=1
        
        return op


            

