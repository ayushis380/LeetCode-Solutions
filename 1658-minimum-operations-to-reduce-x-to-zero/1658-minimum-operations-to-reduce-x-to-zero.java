class Solution {
    public int minOperations(int[] nums, int x) {
        int total=0, maxLen = -1, left =0, curr=0;
        int len = nums.length;
        for(int val: nums){
            total+= val;
        }
        for(int right=0; right<len ; right++){
            curr+= nums[right];
            while(curr> total-x && left<= right){
                curr-=nums[left];
                left++;
            }
            if(curr== total -x)
                maxLen = Math.max(maxLen, right- left+1);
        }
        return maxLen!= -1 ? len -maxLen: -1;
    }
}