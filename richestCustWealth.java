// 1672. Richest Customer Wealth
// [Easy]
class Solution {
    public int maximumWealth(int[][] accounts) {
        int m = accounts.length;
        int n = accounts[0].length;
        int lsum=0; // to store the largest sum
        for(int i=0; i<m; i++){
            int sum =0;
            for(int j=0; j<n; j++) {
                sum+= accounts[i][j];
            }
         lsum= Math.max(lsum,sum);   
        }
        return lsum;
    }
}
