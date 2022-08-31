class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0; i< numRows; i++){
            List<Integer> temp = new ArrayList<>();
            for(int j=0; j<=i; j++){
                temp.add(1);
            }
            res.add(temp);
        }
        for(int i=2; i< numRows; i++){
           for(int j=1; j<=i-1; j++){
               int val = res.get(i-1).get(j-1) + res.get(i-1).get(j);
               res.get(i).set(j,val);
           }
           
        }
        return res;
    }
}