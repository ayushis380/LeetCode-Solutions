class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> hs = new HashSet<>();
        int start =0, len =0;
        for(int end=0; end< s.length(); end++){
            while(hs.contains(s.charAt(end))){
                hs.remove(s.charAt(start));
                start++;
            }
            hs.add(s.charAt(end));
            len = Math.max(len, end-start+1);
        }
        return len;
    }
}