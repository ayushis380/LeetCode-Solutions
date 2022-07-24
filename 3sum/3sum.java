class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        for(int i=0; i< nums.length && nums[i] <=0; i++){
            if(i ==0 || nums[i-1]!= nums[i])
                helper(nums, i, res);
        }
        return res;
    }
    public void helper(int[] nums, int i, List<List<Integer>> res){
         int l = i+1; 
         int h = nums.length -1;
             while(l < h){
                 int val = nums[i];
                 int sum = nums[l] + nums[h];
                 if(sum > -val)
                     h--;
                 else if(sum< -val)
                     l++;
                 else {
                     res.add(Arrays.asList(nums[i], nums[l++], nums[h--]));
                     while(l< h && nums[l] == nums[l-1])
                         l++;
                 }
                     
             }
    }
}