class Solution {
    public int maxSubArray(int[] nums) {
        int global_sum = Integer.MIN_VALUE;
        int lsum = 0;
        for(int i=0; i< nums.length; i++){
            lsum = Math.max(nums[i], lsum+ nums[i]);
            if(lsum>global_sum)
                global_sum = lsum;
        }
        return global_sum;
    }
}