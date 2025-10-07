class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = list()
        mapper = dict()
        for num in nums2:
            while stack and num>stack[-1]:
                mapper[stack.pop()] = num
            stack.append(num)
        return [mapper[num] if num in mapper else -1 for num in nums1]