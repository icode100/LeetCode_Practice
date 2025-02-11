class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        nums = [(num,i) for i,num in enumerate(nums)]
        def merge(left,right):
            nonlocal counter
            i,j,flag = 0,0,0
            merged = list()
            while i<len(left) and j<len(right):
                if left[i][0] > right[j][0]: 
                    merged.append(right[j])
                    flag += 1 
                    j += 1
                else:
                    merged.append(left[i])
                    counter[left[i][1]] += flag  
                    i += 1
            while i<len(left):
                merged.append(left[i])
                counter[left[i][1]]+=flag
                i+=1
            while j<len(right):
                merged.append(right[j])
                j+=1
            return merged
                    
        def recursion(nums):
            nonlocal counter
            if len(nums)==1: return nums
            mid = len(nums)>>1
            left = recursion(nums[:mid])
            right = recursion(nums[mid:])
            return merge(left,right)

        recursion(nums)
        return [counter[i] for i in range(len(nums))]