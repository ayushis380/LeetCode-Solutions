class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        res[0] = 1;
        int R =1;
        for(int i=1; i< nums.length; i++){
            res[i] = res[i-1] * nums[i-1];
        }
        for(int i= nums.length-1; i >=0; i--){
            res[i] = res[i] *R;
            R= R* nums[i];
        }
        return res;
    }
}
// 4 5 1 8 2
// 1 4 20 20 160
// 80 16 16 2 1

// 80 64 320 40 160
