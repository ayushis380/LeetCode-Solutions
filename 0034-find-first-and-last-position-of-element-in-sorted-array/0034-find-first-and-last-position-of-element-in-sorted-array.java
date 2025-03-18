class Solution {
    public int start = -1, end = -1;
    public int[] searchRange(int[] nums, int target) {
        int low =0, high = nums.length-1;
        int mid;
        while(low <= high){
            mid = low + (high-low)/2;
            if(nums[mid] == target){
                find_start_end(mid, nums, target);
                return new int[]{start,end};
            }
            else if(nums[mid] > target)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return new int[]{-1,-1};
    }
    public void find_start_end(int ind, int[] nums, int target){
        int ind_copy = ind;
        while(ind >=0 && nums[ind] == target){
            start = ind;
            ind--;
        }
        while(ind_copy < nums.length && nums[ind_copy] == target){
            end = ind_copy;
            ind_copy++;
        }
    }
}