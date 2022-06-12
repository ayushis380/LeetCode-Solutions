class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int res=0, start=0, currSum=0;
        Set<Integer> s = new HashSet<>();
        for(int end =0; end< nums.length; end++){
            while(s.contains(nums[end])){
                s.remove(nums[start]);
                currSum-= nums[start];
                start++;
            }
            currSum+= nums[end];
            s.add(nums[end]);
            res = Math.max(res, currSum);
        }
        return res;
    }
}