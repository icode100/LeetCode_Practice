class Solution:
    def __init__(self):
        self.mod = int(1e9+7)
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        N = len(nums)
        # similar to number of subarrays with xor k but here there are two ks

        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)
        hashmap2[0] = 1
        way1 = 0
        way2 = 0
        current = 0
        for num in nums:
            current^=num
            way1 = hashmap2[current^target1]
            way2 = hashmap1[current^target2]
            hashmap1[current]+=way1
            hashmap2[current]+=way2
        return (way1+way2)%self.mod
        


