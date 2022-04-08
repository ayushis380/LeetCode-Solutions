/* 209. Minimum Size Subarray Sum
[Medium]
*/ 
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int start=0, len = nums.length, sum=0;
        int minLen = len;
        boolean flag = false;
        for(int end =0; end< len; end++){
            sum+= nums[end];
            while(sum >= target){
             flag = true;
              minLen= Math.min(minLen, end-start+1);
               sum-= nums[start];
                start++;
            }
        }
        if(flag == true)
            return minLen;
        else 
            return 0;
    }
}
