class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->a[0]-b[0]);
        // int j=1;
        for(int i=0; i< intervals.length-1; i++){
            if(intervals[i+1][0] < intervals[i][1]) // compare 0,1 with 1,0           
                return false;
            }
        return true;
        }
    
}