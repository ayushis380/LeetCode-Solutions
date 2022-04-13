class Solution {
    public int longestOnes(int[] nums, int k) {
        int start=0, maxCount =0, count=0,len=0;
        for(int end =0; end< nums.length; end++){
            if(nums[end] == 1)
                count++;
            maxCount = Math.max(maxCount, count);
            while(end- start+1 -maxCount> k){
                if(nums[start]==1)
                    count--;
                start++;
            }
            len = Math.max(len, end-start+1);
        }
        return len;
    }
}