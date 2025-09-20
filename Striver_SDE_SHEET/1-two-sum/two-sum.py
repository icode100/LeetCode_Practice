class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(list)
        for i,num in enumerate(nums): hashmap[num].append(i)
        nums.sort()
        N = len(nums)
        i,j = 0,N-1
        while i<=j:
            if nums[i]+nums[j]==k:
                temp = []
                temp.append(hashmap[nums[i]].pop())
                temp.append(hashmap[nums[j]].pop())
                return temp
            if nums[i]+nums[j]<k: i+=1
            else: j-=1