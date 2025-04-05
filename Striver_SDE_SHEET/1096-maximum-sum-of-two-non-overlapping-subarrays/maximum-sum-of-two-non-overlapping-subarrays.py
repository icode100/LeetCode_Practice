
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:

# * two cases: L occurs first then M (OR) M occurs first then L handle them separately
# * prefix = accummulate(nums) // prefix array
# * first option for L => nums[0:L] thus max_lsum = prefix[L-1]; first option for M max_msum = prefix[M-1]
# * AIM: Maximizing lsum and msum hence maximizing lsum+msum
# * case 1: L occurs before M
#     * start iteration from L+M so that we dont get out of bound
#     * current msum = prefix[i]-prefix[i-M]
#     * current lsum = prefix[i-M]-prefix[i-M-L]
#     * max_lsum = max(max_lsum,lsum)
#     * ans = max(ans, msum+max_lsum)
# * case 2: M occurs before L
#     * do the same try maximizing msum and then maximize current lsum + max_msum
# return ans

        N = len(A)
        prefix = list(accumulate(A))
        max_lsum,max_msum = prefix[L-1],prefix[M-1]
        ans = prefix[L+M-1]
        for i in range(L+M,N):
            msum = prefix[i]-prefix[i-M]
            lsum = prefix[i]-prefix[i-L]
            max_lsum = max(max_lsum, prefix[i-M]-prefix[i-M-L])
            max_msum = max(max_msum, prefix[i-L]-prefix[i-L-M])
            ans = max(ans, max_lsum + msum, max_msum + lsum)
        return ans
            