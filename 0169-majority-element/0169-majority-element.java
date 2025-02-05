class Solution {
    public int majorityElement(int[] nums) {
      int el = nums[0];
      int count = 0;
      for(int i = 0; i< nums.length; i++){
        if(count == 0)
            el = nums[i];
        if(el == nums[i])
            count++;
        else {
            count--;
        }
      }
      return el;  
    }
}