class Solution {
    public int candy(int[] ratings) {
        int[] can = new int[ratings.length];
        Arrays.fill(can,1);
        boolean change = true;
        while(change){
            change = false;
            for(int i=0; i< ratings.length; i++){
                if(i>0 && ratings[i] > ratings[i-1] && can[i] <= can[i-1]){
                    can[i] = can[i-1] +1;
                    change = true;
                }
                if(i!= ratings.length-1 && ratings[i] > ratings[i+1] && can[i] <= can[i+1]){
                        can[i] = can[i+1] +1;
                        change = true;
                    }
                
            }
        }
        int sum =0;
        for(int val: can){
             sum+= val;
            // System.out.println(val);
        }
        return sum;
           
    }
}