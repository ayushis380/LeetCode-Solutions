class Solution {
    private int size;
    public int totalNQueens(int n) {
         size =n;
        return helper(0, new HashSet<>(), new HashSet<>(), new HashSet<>());
    }
    
    private int helper(int row, Set<Integer> diagonals, Set<Integer> antiDiagonals, Set<Integer> cols){
        if(row == size){
            return 1;
        }
        int count =0;
        for(int col =0; col< size; col++){
            int currDiag = row-col;
            int currAntiDiag = row+ col;
            if(cols.contains(col) || diagonals.contains(currDiag) || antiDiagonals.contains(currAntiDiag))
                continue;
            cols.add(col);
            diagonals.add(currDiag);
            antiDiagonals.add(currAntiDiag);
           
            count += helper(row+1, diagonals, antiDiagonals, cols);
            
            cols.remove(col);
            diagonals.remove(currDiag);
            antiDiagonals.remove(currAntiDiag);
        }
        return count;
    }
}