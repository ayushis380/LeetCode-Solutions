class Solution {
    public int maxSubArray(int[] nums) {
        int gsum=0, lsum = Integer.MIN_VALUE;
        for(int i=0; i< nums.length; i++){
            gsum = Math.max(nums[i], gsum+ nums[i]);
            if(gsum> lsum)
                lsum = gsum;
        }
        return lsum;
    }
}