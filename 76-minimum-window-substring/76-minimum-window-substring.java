class Solution {
    public String minWindow(String s, String t) {
        int sl= s.length();
        int tl = t.length();
        String res ="";
        if(tl > sl)
            return "";
        int[] smap = new int[128];
        int[] tmap = new int[128];
        for(int i=0; i< tl; i++) tmap[t.charAt(i)]++;
        int start=0, minLen = sl;
        for(int end =0; end< sl; end++){
            smap[s.charAt(end)]++;
            while(check(tmap, smap) == true){
                if(minLen >= end-start+1){
                    minLen = Math.min(minLen, end-start+1);
                    res= s.substring(start, end+1);
                }
                smap[s.charAt(start)]--;
                start++;
            }
        }
       return res; 
    }
    public boolean check(int[] tmap , int[] smap){
        for(int i=0; i< 127; i++){
            if(smap[i] < tmap[i])
                return false;
        }
        return true;
    }
}