class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int len = cardPoints.length -k;
        int totalSum=0, windSum=0, start=0;
        for(int val: cardPoints){
            totalSum+= val;
        }
        if(k ==cardPoints.length )
            return totalSum;
        int minValue= totalSum;
        for(int i=0; i< cardPoints.length; i++){
            windSum += cardPoints[i];
            if(i -len >=-1){
                minValue = Math.min(minValue, windSum);
                windSum-= cardPoints[start];
                start++;
            }
        }   
        return totalSum- minValue;
    }
}       