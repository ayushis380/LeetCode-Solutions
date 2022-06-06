class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int count =0;
        Arrays.sort(nums);
        for(int i=0; i< nums.length -2 ; i++){
            count+= check(nums, i+1, target- nums[i]);
        }
        return count;
    }
    private int check(int[] nums, int s, int target){
       int sum=0, left= s, right = nums.length-1;
        while(left < right){
            if(nums[left] + nums[right] < target){
                sum+= right- left;
                left++;
            }
            else
                right--;
        }
        return sum;
    }
}