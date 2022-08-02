class Solution {
    public int compareVersion(String version1, String version2) {
        String[] farr = version1.split("\\.");
        String[] sarr = version2.split("\\.");
        int i1, i2;
        for(int i=0; i< Math.max(farr.length, sarr.length); i++){
            i1 = i < farr.length ? Integer.parseInt(farr[i]): 0;
            i2 = i < sarr.length ? Integer.parseInt(sarr[i]): 0;
            if(i1 != i2)
                return i1<i2 ? -1:1;
        }
        return 0;
    }
}