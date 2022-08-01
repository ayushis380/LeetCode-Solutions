class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] lprod = new int[nums.length];
        int[] rprod = new int[nums.length];
        Arrays.fill(lprod,1);
        Arrays.fill(rprod,1);
        for(int i=1; i< nums.length; i++){
            lprod[i] = lprod[i-1] * nums[i-1];
        }
        for(int i= nums.length -2 ; i>=0 ;i--){
            rprod[i] = rprod[i+1] * nums[i+1];
        }
        for(int i=0; i< nums.length; i++){
            nums[i] = lprod[i] * rprod[i];
        }
        return nums;
    }
}