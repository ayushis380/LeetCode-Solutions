class Solution {
    private int size;
    private List<List<String>> res = new ArrayList<List<String>>();
    public List<List<String>> solveNQueens(int n) {
        size =n;
        char[][] empBoard = new char[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j< n; j++){
                empBoard[i][j] = '.';
            }
        }
        helper(0, new HashSet<>(), new HashSet<>(), new HashSet<>(), empBoard);
        return res;
    }
    private void helper(int row, Set<Integer> diagonals, Set<Integer> antiDiagonals, Set<Integer> cols, char[][] state){
        if(row == size){
            res.add(createBoard(state));
            return;
        }
        for(int col =0; col< size; col++){
            int currDiag = row-col;
            int currAntiDiag = row+ col;
            if(cols.contains(col) || diagonals.contains(currDiag) || antiDiagonals.contains(currAntiDiag))
                continue;
            cols.add(col);
            diagonals.add(currDiag);
            antiDiagonals.add(currAntiDiag);
            state[row][col] = 'Q';
            helper(row+1, diagonals, antiDiagonals, cols, state);
            
            cols.remove(col);
            diagonals.remove(currDiag);
            antiDiagonals.remove(currAntiDiag);
            state[row][col] = '.';
        }
    }
    private List<String> createBoard(char[][] state){
        List<String> board = new ArrayList<String>();
        for(int row=0; row< size; row++){
            String crow = new String(state[row]);
            board.add(crow);
        }
      return board;  
    }
}