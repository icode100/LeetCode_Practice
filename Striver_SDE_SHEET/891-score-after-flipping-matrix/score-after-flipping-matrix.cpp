class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        // row optimization
        for(int i=0;i<m;i++){
            if(grid[i][0]==0){
                for(int j=0;j<n;j++){
                    grid[i][j] = 1-grid[i][j];
                }
            }
        }

        // optimize columns
        for(int j=0;j<n;j++){
            int count = 0;
            for(int i=0;i<m;i++){
                count+=grid[i][j]==0?1:0;
            }
            if(count>m-count){
                for(int i=0;i<m;i++){
                    grid[i][j] = 1-grid[i][j];
                }
            }
        }

        int score = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int columnScore = grid[i][j] << (n - j - 1);
                score += columnScore;
            }
        }
        return score;
    }
};