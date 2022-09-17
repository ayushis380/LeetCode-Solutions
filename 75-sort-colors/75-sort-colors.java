class Solution {
    public void sortColors(int[] nums) {
        int high = nums.length-1;
        int low = 0, mid=0;
        int temp =0;
        while(mid <= high){
            if(nums[mid] ==0){
                temp = nums[mid];
                nums[mid++] = nums[low];
                nums[low++] = temp;
            }
            else if(nums[mid] ==1){
                mid++;
            }
            else{
                temp = nums[mid];
                nums[mid] = nums[high];
                nums[high--] = temp;
            }
            
        }
    }
}