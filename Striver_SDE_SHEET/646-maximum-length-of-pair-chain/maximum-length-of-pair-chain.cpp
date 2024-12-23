class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        int n = pairs.size();
        sort(pairs.begin(), pairs.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1]; 
        });
        int prev = pairs[0][1], chains=1;
        for(int i=1;i<n;i++){
            if(pairs[i][0]>prev){
                chains+=1;
                prev = pairs[i][1];
            }
        }
        return chains;
    }
};