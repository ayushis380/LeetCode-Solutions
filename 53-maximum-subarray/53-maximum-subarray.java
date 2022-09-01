class Solution {
    public int maxSubArray(int[] nums) {
        int lsum=0, gsum = Integer.MIN_VALUE;
        for(int i=0; i< nums.length; i++){
            lsum = Math.max(nums[i], lsum+ nums[i]); // local sum- comparing new and old value
            if(lsum> gsum) // global sum check
                gsum = lsum; // replace only if the local sum is greater than the global sum 
        }
        return gsum; // return the global sum - this is the max in the array
    }
}