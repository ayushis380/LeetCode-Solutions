/* 53. Maximum Subarray
[Easy]
*/
class Solution {
    public int maxSubArray(int[] nums) {
        int sum= 0, lsum = Integer.MIN_VALUE;
        for(int end =0; end < nums.length ; end++){
            sum = Math.max(nums[end], sum+ nums[end]);
            if(sum > lsum)
                lsum = sum;
        }
        return lsum;
    }
}
