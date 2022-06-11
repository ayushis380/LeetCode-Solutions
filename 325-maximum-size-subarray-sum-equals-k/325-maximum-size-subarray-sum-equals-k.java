class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        int pfsum =0, maxLen =0;
        Map<Integer, Integer> m = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            pfsum+= nums[i];
            if(pfsum == k){
                maxLen = i+1; 
            }
            if(m.containsKey(pfsum-k)){
                maxLen = Math.max(maxLen, i - m.get(pfsum-k));
            }
            if(!m.containsKey(pfsum))
                m.put(pfsum, i);    
        }
        return maxLen;
    }
}