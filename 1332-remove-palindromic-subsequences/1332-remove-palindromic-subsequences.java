class Solution {
    public int removePalindromeSub(String s) {
        if(s.isEmpty())
            return 0;
        StringBuilder str = new StringBuilder(s);
        str.reverse();
        String revStr = str.toString();
        if(s.equals(revStr))
            return 1;
        return 2;
        
    }
}