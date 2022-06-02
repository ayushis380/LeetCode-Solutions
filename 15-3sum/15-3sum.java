class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0; i< nums.length && nums[i]<=0 ; i++){
            if(i==0 || nums[i-1]!= nums[i])
                check(nums, res, i);
        }
         return res;
     }
    public void check(int[] nums, List<List<Integer>> res, int i){
       int l= i+1, h= nums.length-1;
        while(l<h){
            int sum = nums[i] +nums[l] + nums[h];
            if(sum>0)
                h--;
            else if(sum<0)
                l++;
            else{
                res.add(Arrays.asList(nums[i], nums[l++], nums[h--]));
                while(l < h && nums[l]== nums[l-1])
                    l++;
            }
                
        }
    }
}