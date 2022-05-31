class Solution {
    public boolean hasAllCodes(String s, int k) {
       Set<String> st = new HashSet<>();
        int req= 1<<k;
        int count=0;
        for(int i=0; i< s.length()- k+1; i++){
            String sub= s.substring(i,i+k);
            st.add(sub);
        }
        return st.size() == req;
        
    }
    
}