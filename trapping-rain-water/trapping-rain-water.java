class Solution {
    public int trap(int[] height) {
        int res =0;
        int len = height.length;
        int[] left_m = new int[len];
        left_m[0] = height[0];
        int[] right_m = new int[len];
        right_m[len-1] = height[len-1];
        for(int i=1; i< len; i++){
            left_m[i] = Math.max(height[i], left_m[i-1]);
        }
        for(int i= len-2; i>=0; i--){
            right_m[i] = Math.max(height[i], right_m[i+1]);
        }
        for(int i= 0; i< len; i++){
            res+= Math.min(left_m[i], right_m[i]) - height[i];
        }
       return res; 
    }
}