class Solution {
public:
    int trap(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        vector<int> left(n,-1);
        vector<int> right(n,-1);
        left[0]=nums[0],right.back() = nums.back();
        for(int i=1;i<n;i++) left[i] = max(left[i-1],nums[i]);
        for(int i=n-2;i>=0;--i) right[i] = max(right[i+1],nums[i]);
        for(int i=1;i<n-1;i++) ans+=  min(left[i],right[i]) - nums[i] < 0?0: min(left[i],right[i]) - nums[i];
        return ans;
    }
};