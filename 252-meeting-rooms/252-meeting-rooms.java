class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->a[0]-b[0]);
        int j=1;
        for(int i=1; i< intervals.length; i++){
            if(intervals[i][j-1] < intervals[i-1][j]) // compare 0,1 with 1,0           
                return false;
            }
        return true;
        }
    
}