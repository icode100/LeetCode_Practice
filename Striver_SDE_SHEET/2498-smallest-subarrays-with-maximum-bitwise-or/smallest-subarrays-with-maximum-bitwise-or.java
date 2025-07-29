class Solution {
    public int[] smallestSubarrays(int[] nums) {
        int N = nums.length;
        int [] pos = new int[31];
        int [] ans = new int[N];
        for(int i=0;i<31;i++) pos[i]=-1;
        for(int i=0;i<N;i++) ans[i]=0;

        for(int i=N-1;i>-1;i--){
            int j = i;
            for(int k=0;k<31;k++){
                if((nums[i] & (1<<k))==0){
                    j=Math.max(j,pos[k]);
                }else{
                    pos[k] = i;
                }
            }
            ans[i] = j-i+1;
        }
        return ans;
    }
}