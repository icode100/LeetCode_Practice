INT_MAX = sys.maxsize
INT_MIN = -INT_MAX-1
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        '''
        * the tree is undirected so we can use stone transfer 
        * so practically there is no significance of the edge right because its a tree so no cycles and undirected so we can choose any two nodes
        * except the number of operations should be even as at a single point we update two nodes and not one
        * so now it boils down to try all possible ways so DP
        '''
        N = len(nums)
        @cache
        def recursion(index,parity):
            if index==N:
                if parity: return 0
                else: return INT_MIN
            pick = (nums[index]^k)+recursion(index+1,not parity)
            notpick = nums[index]+recursion(index+1,parity)
            return max(pick,notpick)
        return recursion(0,True)


        
