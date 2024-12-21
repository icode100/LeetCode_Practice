class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int curr = 0;
        for(int i=0;i<n;i++){
            if(i>curr) return false;
            curr = max(curr,nums[i]+i);
        }
        return true;
    }
};