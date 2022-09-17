class Solution {
    public void nextPermutation(int[] nums) {
       if(nums.length ==1)
           return;
        int n = nums.length-1;
        int small=-1, big =0;
        for(int i=n; i>0; i--){
            if(nums[i] > nums[i-1]){
                small = i-1;
                break;
            }
                
        }
        int j=n;
        if(small>=0){
            while(small >=0 && nums[small] >= nums[j]){
           j--;
        }
        swap(nums, small, j);
        }
        reverse(nums, small+1, n);
    }
    public void reverse(int[] nums, int i, int j){
        while(i<j){
            swap(nums, i++,j--);
        }
    }
    public void swap(int[] nums, int small, int big){
        int temp = nums[small];
        nums[small] = nums[big];
        nums[big] = temp;
    }
}