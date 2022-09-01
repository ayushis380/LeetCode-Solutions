class Solution {
    public int maxProfit(int[] prices) {
        int minp = Integer.MAX_VALUE;
        int global_maxp = 0;
        for(int i=0; i< prices.length; i++){
            if(prices[i] < minp)
                minp = prices[i];
            if(prices[i]-minp > global_maxp ){
                global_maxp = prices[i] - minp;
            }
        }
        return global_maxp;
    }
}