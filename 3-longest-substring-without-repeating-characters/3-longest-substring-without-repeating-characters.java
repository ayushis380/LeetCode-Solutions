class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start =0, maxlen = 0;
        int[] count = new int[128];
        for(int end =0; end< s.length(); end++){
            // System.out.println(s.charAt(end));
            count[s.charAt(end)]++;
            while(count[s.charAt(end)] > 1){
                count[s.charAt(start)]--;
                start++;
            }
            maxlen = Math.max(maxlen, end-start+1);
            
        }
        return maxlen;
    }
}