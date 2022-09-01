class Solution {
    public void sortColors(int[] nums) {
        int len = nums.length;
        int[] arr = new int[3];
        for(int i=0; i< len; i++){
            if(nums[i]==0)
                arr[0]++;
            else if(nums[i]==1)
                arr[1]++;
            else if(nums[i]==2)
                arr[2]++;
        }
        for(int i=0; i< arr[0];i++){
            nums[i] =0;
        }
        for(int i=arr[0]; i< arr[0]+arr[1];i++){
            nums[i] =1;
        }
        for(int i=arr[0]+arr[1]; i< arr[0]+arr[1]+arr[2];i++){
            nums[i] =2;
        }
    }
}