class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sortednums = sorted(nums)
        # print(sortednums)
        N = len(nums)
        groups = list()
        group = deque([sortednums[0]])
        # print(group)
        for i in range(1,N):
            # print(group,groups)
            if abs(sortednums[i]-sortednums[i-1])<=limit: group.append(sortednums[i])
            else:
                groups.append(deque(group.copy()))
                group = deque([sortednums[i]])
        groups.append(group)
        ele2grp = {}
        for i,group in enumerate(groups):
            for num in group: ele2grp[num] = i
        proxy = list()
        # for i in nums: proxy[i] = ele2grp[i]
        # print(groups)
        return [groups[ele2grp[i]].popleft() for i in nums]
