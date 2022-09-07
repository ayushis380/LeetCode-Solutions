class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int low = 0; int m = matrix.length;
        int n = matrix[0].length;
        int high = m * n -1;
        while(low<= high){
            int mid = (low+high)/2;
            int val = matrix[mid/n][mid%n];
            if(val == target)
                return true;
            else if(val >= target){
                high = mid-1;
            }
            else
                low = mid+1;
        }
        return false;
    }
}