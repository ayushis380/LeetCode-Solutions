class Solution {
    public int strStr(String haystack, String needle) {
        int hayLen = haystack.length();
        int nLen = needle.length();
        if(nLen > hayLen )
            return -1;
        for(int i=0; i< hayLen- nLen +1; i++){
            String str = haystack.substring(i, i+nLen);
            if(str.equals(needle))
                return i;
        }
        return -1;
    }
}