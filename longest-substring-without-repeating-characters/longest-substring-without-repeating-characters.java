class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> m = new HashMap<>();
        int len=0; int start =0;
        for(int end=0; end< s.length(); end++){
            char ch = s.charAt(end);
            m.put(ch, m.getOrDefault(ch,0)+1);
            while(m.get(ch) >1){
                char chstart = s.charAt(start++);
                m.put(chstart, m.getOrDefault(chstart,0)-1);
            }
            len = Math.max(len, end-start+1);
        }
         return len;
        }
       
    }