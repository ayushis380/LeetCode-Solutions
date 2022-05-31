class Solution {
    public boolean hasAllCodes(String s, int k) {
        int req = (int)Math.pow(2,k) -1;
        int[] arr = new int[req+1];
        int count=0;
        int len = s.length();
        for(int i=0; i< len-k+1; i++){
            String str= s.substring(i, i+k);
            int val = helper(str,k);
            if(val<=req && arr[val] == 0){
                arr[val]++;
                count++;
            }
                
        }
        // System.out.println
        return count == req+1;
        
    }
    public int helper(String str, int k){
        int val=0;
        for(int i=k-1; i>=0; i--){
            val+= Character.getNumericValue(str.charAt(i)) * Math.pow(2, k-i-1);
        }
        return val;
    }
}