class Solution {
    public int minMoves2(int[] nums) {
        int len = nums.length;
        if(len ==1)
            return 0;
        Arrays.sort(nums);
        int median, count =0;
        int mid = len/2;
        if(len >>1 ==0){ // divide by 2
            median = (nums[mid-1] + nums[mid])/2; 
        }else{
            median = nums[mid];
        }
        for(int val: nums){
            count+= Math.abs(median - val);
        }
        return count;
    }
}