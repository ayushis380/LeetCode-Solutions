class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length()> s2.length())
            return false;
        int[] s1m = new int[26];
        int[] s2m = new int[26];
        for(int i=0; i< s1.length(); i++){
            s1m[s1.charAt(i) - 'a']++;
            s2m[s2.charAt(i) - 'a']++;
        }
        for(int i=0; i< s2.length() - s1.length(); i++){
            if(check(s1m, s2m) == true)
                return true;
            s2m[s2.charAt(i+s1.length()) - 'a']++;
            s2m[s2.charAt(i) - 'a']--;
        }
        return check(s1m, s2m);      
}
    public boolean check(int[] s1m, int[] s2m){
        for(int i=0; i<26; i++){
            if(s1m[i] != s2m[i])
                return false;
        }
        return true;
    }
}