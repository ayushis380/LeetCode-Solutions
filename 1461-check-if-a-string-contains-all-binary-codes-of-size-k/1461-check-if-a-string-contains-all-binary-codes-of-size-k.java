class Solution {
    public boolean hasAllCodes(String s, int k) {
        int req= 1<<k;
        boolean[] check = new boolean[req];
        int allOne = req-1;
        int hv= 0;
        for(int i=0; i< s.length(); i++){
            hv = ((hv <<1 ) & allOne) | (s.charAt(i)-'0');
            if(i>= k-1 && !check[hv]){
                check[hv] = true;
                req--;
                if(req== 0)
                    return true;
            }
        }
        return false;
        
    }
    
}