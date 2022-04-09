/* 340. Longest Substring with At Most K Distinct Characters
[Medium]
*/
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> m = new HashMap<>();
        int start =0, len=0;
        for(int end =0; end< s.length(); end++){
            char val = s.charAt(end);
            m.put(val, m.getOrDefault(val,0)+1);
            while(m.size() > k){
                m.put(s.charAt(start), m.get(s.charAt(start))-1); // shriking the sliding window
                if(m.get(s.charAt(start)) == 0)
                    m.remove(s.charAt(start)); // removing character as its not a part of valid substring
                start++;
            }
            len = Math.max(len, end-start+1);
        }
        return len;
    }
}
