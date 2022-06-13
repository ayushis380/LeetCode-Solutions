class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        for(int row =1; row<triangle.size(); row++){
            for(int col =0; col<= row; col++){
                int smallVal = Integer.MAX_VALUE;
                if(col>0)
                    smallVal = triangle.get(row-1).get(col-1);
                if(col< row)
                    smallVal = Math.min(smallVal, triangle.get(row-1).get(col));
                int sum = smallVal + triangle.get(row).get(col);
                triangle.get(row).set(col, sum);
            }
        }
        return Collections.min(triangle.get(triangle.size()-1));
    }
}