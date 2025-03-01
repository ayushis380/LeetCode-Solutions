class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        reverse(0, n-1-k, nums); // reverse the starting (total -k) positions first as we need to shift right
        reverse(n-k, n-1, nums); // then k positions 
        reverse(0, n-1, nums); // reverse full array - now to place everything at correct position
        // this way we dont use extra space 
    }
    public void reverse(int start, int end, int[] nums){
        while (start <= end)
        {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}