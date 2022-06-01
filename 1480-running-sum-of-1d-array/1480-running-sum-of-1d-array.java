class Solution {
    public int[] runningSum(int[] nums) {
        int rsum = 0;
        // int[] res = new int[nums.length];
        for(int i=0; i<nums.length ; i++){
            rsum+= nums[i];
            nums[i] = rsum;
        }
        return nums;
        
    }
}