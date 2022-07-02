class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a, b) -> Integer.compare(b[1], a[1]));
        int res=0;
        for(int[] val: boxTypes){
            if(truckSize >= val[0]){
                res+= val[0] * val[1];
                truckSize-= val[0];
            }else{
                res+= truckSize * val[1];
                return res;
            }
        }
        return res;
    }
}