class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        if(s.length()< p.length())
            return res;
        int[] smap = new int[26];
        int[] pmap = new int[26];
        for(int i=0; i< p.length(); i++){
            smap[s.charAt(i) - 'a']++;
            pmap[p.charAt(i) - 'a']++;
        }
        if(check(smap, pmap) == true)
            res.add(0);
        for(int i=0; i< s.length()- p.length(); i++){
            smap[s.charAt(i+p.length()) -'a']++;
            smap[s.charAt(i) - 'a']--;
            if(check(smap, pmap) == true)
                res.add(i+1);
        }
        return res;
    }
    public boolean check(int[] smap, int[] pmap){
        for(int i=0; i< 26; i++){
            if(smap[i] != pmap[i])
                return false;
        }
        return true;
    }
}