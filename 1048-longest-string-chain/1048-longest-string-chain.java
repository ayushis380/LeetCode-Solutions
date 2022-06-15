class Solution {
    public int longestStrChain(String[] words) {
        Map<String, Integer> m = new HashMap<>();
        Set<String> s = new HashSet<>();
        Collections.addAll(s,words);
        int ans =0;
        for(String str: words){
            ans = Math.max(ans, helper(s, m, str));
        }
        return ans;
    }
    public int helper(Set<String> s, Map<String, Integer> m, String str){
        if(m.containsKey(str))
            return m.get(str);
        int maxLen = 1;
        StringBuilder sb = new StringBuilder(str);
        for(int i=0; i< str.length(); i++){
            sb.deleteCharAt(i);
            String nword = sb.toString();
            if(s.contains(nword)){
                int currLen = 1+ helper(s,m,nword);
                maxLen = Math.max(maxLen, currLen);
            }
            sb.insert(i, str.charAt(i));
        }
        m.put(str, maxLen);
        return maxLen;
    }
}