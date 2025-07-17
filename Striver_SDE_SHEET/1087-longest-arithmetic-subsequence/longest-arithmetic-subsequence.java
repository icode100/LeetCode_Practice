class Solution {
    public int longestArithSeqLength(int[] nums) {
        int N = nums.length;
        Map<Integer,Map<Integer,Integer>> dp = new HashMap<>();
        for(int i=0;i<N;i++){
            dp.put(i,new HashMap<Integer,Integer>());
            for(int j=0;j<i;j++){
                dp.get(i).put(nums[i]-nums[j], 1+dp.get(j).getOrDefault(nums[i]-nums[j],1));
            }
        }
        return dp.values().stream().flatMap(m->m.values().stream()).max(Integer::compare).orElse(0);
    }
}