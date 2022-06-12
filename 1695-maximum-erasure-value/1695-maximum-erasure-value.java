class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int res=0, start=0;
        int n = nums.length;
        int[] psum = new int[n+1];
        Map<Integer, Integer> m = new HashMap<>();
        for(int end =0; end<n; end++){
            int curr = nums[end];
            psum[end+1] = psum[end] +curr;
            if(m.containsKey(curr))
                start= Math.max(start, m.get(curr)+1);
            res = Math.max(res, psum[end+1] - psum[start]);
            m.put(curr, end);
        }
        return res;
    }
}